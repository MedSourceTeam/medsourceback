from rest_framework import generics
from medsource.serializers import PatientSerializer
from medsource.models import Patient


class PatientRegistView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer