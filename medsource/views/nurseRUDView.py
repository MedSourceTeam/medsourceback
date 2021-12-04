from medsource.models import Nurse
from medsource.serializers import NurseSerializer
from rest_framework import generics


class NurseRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    lookup_field = 'identification'
