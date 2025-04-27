from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from clients.models import Client, HealthProgram, Enrollment
from django.contrib.auth.models import User
from datetime import date

class ClientAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='apiuser', password='apipass')
        self.client.login(username='apiuser', password='apipass')

        self.program = HealthProgram.objects.create(name='Malaria', description='Malaria program')
        self.client_obj = Client.objects.create(
            first_name='Bob',
            last_name='Builder',
            date_of_birth=date(1980, 1, 1),
            gender='M'
        )
        Enrollment.objects.create(client=self.client_obj, program=self.program)

    def test_client_list(self):
        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_client_detail(self):
        url = reverse('client-detail', args=[self.client_obj.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Bob')
        self.assertIn('programs', response.data)
