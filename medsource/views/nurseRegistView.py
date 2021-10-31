from rest_framework import generics
from medsource.serializers import NurseSerializer
from medsource.models import Nurse


class NurseRegistView(generics.CreateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
