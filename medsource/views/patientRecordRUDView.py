from medsource.models import Patient_Record
from medsource.serializers import Patient_RecordSerializer
from rest_framework import generics


class PatientRecordRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient_Record.objects.all()
    serializer_class = Patient_RecordSerializer
