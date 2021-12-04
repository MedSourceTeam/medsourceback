from medsource.models import Patient
from medsource.serializers import PatientSerializer
from rest_framework import generics


class PatientRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'identification'
