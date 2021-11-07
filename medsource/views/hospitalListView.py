from rest_framework import generics
from medsource.models import Hospital
from medsource.serializers import HospitalSerializer


class HospitalListView(generics.ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
