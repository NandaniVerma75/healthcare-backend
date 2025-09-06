from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Patient
from .serializers import PatientSerializer, PatientListSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    """
    GET: List all patients for the authenticated user
    POST: Create a new patient
    """
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PatientListSerializer
        return PatientSerializer