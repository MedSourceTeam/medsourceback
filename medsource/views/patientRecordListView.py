from django.db.models import query
from rest_framework.serializers import Serializer
from medsource import serializers
from medsource.models import Patient_Record, Record
from medsource.serializers import ShowPatientRecordsSerializer
from rest_framework import generics


class PatientRecordListView(generics.ListAPIView):
    serializer_class = ShowPatientRecordsSerializer
    queryset = Patient_Record.objects.all()