from rest_framework import serializers
from medsource.models import Patient_Record

class ShowPatientRecordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient_Record
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'patient_identification' : instance.patient.identification,
            'patient_name' : instance.patient.full_name,
            'record_name' : instance.record.name,
            'record_kind' : instance.record.kind,
            'record_sort' : instance.record.sort
        }