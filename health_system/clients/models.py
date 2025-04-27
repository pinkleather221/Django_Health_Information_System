from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator

class HealthProgram(models.Model):
    """Model representing a health program (e.g., TB, Malaria, HIV)"""
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex='^[a-zA-Z ]+$',
                message='Name can only contain letters and spaces'
            )
        ]
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Health Program'
        verbose_name_plural = 'Health Programs'

    def __str__(self):
        return self.name

class Client(models.Model):
    """Model representing a client/patient in the system"""
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )
    address = models.TextField(blank=True)
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            RegexValidator(
                regex='^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'"
            )
        ]
    )
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    programs = models.ManyToManyField(
        HealthProgram,
        through='Enrollment',
        related_name='clients'
    )

    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = ['first_name', 'last_name', 'date_of_birth']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Enrollment(models.Model):
    """Through model for client-program relationships"""
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    program = models.ForeignKey(
        HealthProgram,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    enrollment_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-enrollment_date']
        unique_together = ('client', 'program')
        verbose_name = 'Program Enrollment'
        verbose_name_plural = 'Program Enrollments'

    def __str__(self):
        return f"{self.client} in {self.program}"