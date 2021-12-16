from django.db.models import query
from rest_framework.serializers import Serializer
from medsource import serializers
from medsource.models import Patient_Record, Record
from medsource.serializers import ShowPatientRecordsSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class PatientRecordListView(generics.ListAPIView):
    serializer_class = ShowPatientRecordsSerializer
    queryset = Patient_Record.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {'patient__identification': ['icontains'],
                        'patient__full_name': ['icontains'],
                        'record__name': ['icontains'],
                        'record__kind': ['icontains'],
                        'record__sort': ['icontains'], }
