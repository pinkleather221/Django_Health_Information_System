from django.urls import path
from . import views

app_name = 'clients'  # Add this for namespace

urlpatterns = [
    # Home/root path (optional)
    path('', views.client_list, name='home'),
    
    # Program paths
    path('programs/', views.program_list, name='program_list'),
    path('programs/create/', views.program_create, name='program_create'),
    
    # Client paths
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('clients/search/', views.client_search, name='client_search'),
    path('clients/<int:client_id>/enroll/', views.enroll_client, name='enroll_client'),
]