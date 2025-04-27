from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from clients.models import Client
from .serializers import ClientSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ClientListAPIView(generics.ListAPIView):
    """
    API view to retrieve list of clients with pagination.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = StandardResultsSetPagination

class ClientDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve a single client by ID.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
