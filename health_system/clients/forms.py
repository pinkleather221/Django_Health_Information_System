from django import forms
from .models import Client, HealthProgram, Enrollment

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class HealthProgramForm(forms.ModelForm):
    class Meta:
        model = HealthProgram
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['program', 'notes']