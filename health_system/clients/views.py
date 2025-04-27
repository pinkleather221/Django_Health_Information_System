from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Client, HealthProgram, Enrollment
from .forms import ClientForm, HealthProgramForm, EnrollmentForm

@login_required
def program_list(request):
    """
    View to list all health programs.
    """
    programs = HealthProgram.objects.all()
    return render(request, 'program_list.html', {'programs': programs})

@login_required
def program_create(request):
    """
    View to create a new health program.
    """
    if request.method == 'POST':
        form = HealthProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = HealthProgramForm()
    return render(request, 'program_form.html', {'form': form})

@login_required
def client_list(request):
    """
    View to list all clients.
    """
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_create(request):
    """
    View to create a new client.
    """
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

@login_required
def client_detail(request, pk):
    """
    View to display client details and their enrollments.
    """
    client = get_object_or_404(Client, pk=pk)
    enrollments = Enrollment.objects.filter(client=client)
    return render(request, 'client_detail.html', {
        'client': client,
        'enrollments': enrollments
    })

@login_required
def client_search(request):
    """
    View to search clients by first name, last name, or phone number.
    """
    query = request.GET.get('q')
    if query:
        clients = Client.objects.filter(
            models.Q(first_name__icontains=query) | 
            models.Q(last_name__icontains=query) |
            models.Q(phone_number__icontains=query)
        )
    else:
        clients = Client.objects.none()
    return render(request, 'client_search.html', {'clients': clients, 'query': query})

@login_required
def enroll_client(request, client_id):
    """
    View to enroll a client in a health program.
    """
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.client = client
            enrollment.save()
            return redirect('client_detail', pk=client.id)
    else:
        form = EnrollmentForm()
    return render(request, 'enroll_form.html', {'form': form, 'client': client})
