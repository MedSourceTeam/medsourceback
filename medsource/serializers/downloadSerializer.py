from rest_framework import serializers
from medsource.models import Development, Patient, Doctor, Nurse, Hospital, Procedure


class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Development
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'date': instance.date,
            'patient_name': instance.patient.full_name,
            'patient_identification': instance.patient.identification,
            'procedure_name': instance.procedure.name,
            'procedure_id': instance.procedure,
            'procedure_uvr': instance.procedure.uvr
        }