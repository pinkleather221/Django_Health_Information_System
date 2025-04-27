from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Client, HealthProgram, Enrollment
from datetime import date

class ClientProgramTests(TestCase):
    def setUp(self):
        # Create a user and login
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create a health program
        self.program = HealthProgram.objects.create(name='TB', description='Tuberculosis program')

    def test_create_client(self):
        response = self.client.post(reverse('client_create'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'gender': 'M',
            'address': '123 Street',
            'phone_number': '+1234567890',
            'email': 'john@example.com',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Client.objects.filter(first_name='John', last_name='Doe').exists())

    def test_enroll_client(self):
        client_obj = Client.objects.create(
            first_name='Jane',
            last_name='Smith',
            date_of_birth=date(1985, 5, 15),
            gender='F'
        )
        response = self.client.post(reverse('enroll_client', args=[client_obj.id]), {
            'program': self.program.id,
            'notes': 'Enrolled for TB treatment',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Enrollment.objects.filter(client=client_obj, program=self.program).exists())

    def test_client_search(self):
        Client.objects.create(
            first_name='Alice',
            last_name='Wonderland',
            date_of_birth=date(1992, 7, 20),
            gender='F'
        )
        response = self.client.get(reverse('client_search') + '?q=Alice')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alice')

    def test_program_list_view(self):
        response = self.client.get(reverse('program_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TB')
