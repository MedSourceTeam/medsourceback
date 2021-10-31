from rest_framework import generics
from medsource.serializers import DoctorSerializer
from medsource.models import Doctor


class DoctorRegistView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
