from rest_framework import generics
from medsource.serializers import Patient_RecordSerializer
from medsource.models import Patient_Record


class Patient_RecordRegistView(generics.CreateAPIView):
    queryset = Patient_Record.objects.all()
    serializer_class = Patient_RecordSerializer