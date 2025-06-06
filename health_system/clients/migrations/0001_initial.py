# Generated by Django 4.2.20 on 2025-04-27 08:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('address', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='HealthProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator(message='Name can only contain letters and spaces', regex='^[a-zA-Z ]+$')])),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Health Program',
                'verbose_name_plural': 'Health Programs',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField(auto_now_add=True)),
                ('notes', models.TextField(blank=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='clients.client')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='clients.healthprogram')),
            ],
            options={
                'verbose_name': 'Program Enrollment',
                'verbose_name_plural': 'Program Enrollments',
                'ordering': ['-enrollment_date'],
                'unique_together': {('client', 'program')},
            },
        ),
        migrations.AddField(
            model_name='client',
            name='programs',
            field=models.ManyToManyField(related_name='clients', through='clients.Enrollment', to='clients.healthprogram'),
        ),
        migrations.AlterUniqueTogether(
            name='client',
            unique_together={('first_name', 'last_name', 'date_of_birth')},
        ),
    ]
