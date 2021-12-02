from rest_framework import serializers
from medsource.models import Patient_Record, Patient, Record


class Patient_RecordSerializer(serializers.ModelSerializer):
    idPatient = serializers.SlugRelatedField(
        write_only=True, queryset=Patient.objects.all(), source='patient', slug_field="identification")

    idRecord = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Record.objects.all(), source='record')

    class Meta:
        model = Patient_Record
        fields = ['patient', 'idPatient', 'record', 'idRecord']
        read_only_fields = ['patient', 'record']
        depth = 1

    def create(self, validated_data):

        patient_recordInstance = Patient_Record.objects.create(
            **validated_data)
        return patient_recordInstance
