from medsource.models import Doctor
from medsource.serializers import DoctorSerializer
from rest_framework import generics


class DoctorRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'identification'
