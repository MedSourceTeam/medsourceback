from rest_framework import serializers
from medsource.models import Consultation, Patient, Doctor, Hospital

class ConsultationSerializer(serializers.ModelSerializer):
    idPatient = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Patient.objects.all(), source='patient')
    idDoctor = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Doctor.objects.all(), source='doctor')
    idHospital = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Hospital.objects.all(), source='hospital')

    class Meta:
        model = Consultation
        fields = ['pulse', 'height', 'weight', 'pa', 'pr', 't', 'medication', 'symptom', 'diagnosis', 'patient', 'idPatient', 'doctor', 'idDoctor', 'hospital', 'idHospital']
        read_only_fields = ['patient', 'doctor', 'hospital']
        depth = 1

    def create(self, validated_data):

        consultationInstance = Consultation.objects.create(**validated_data)
        return consultationInstance