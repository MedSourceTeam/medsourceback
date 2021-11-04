from rest_framework import serializers
from medsource.models import Development, Patient, Doctor, Nurse, Hospital, Procedure

class DevelopmentSerializer(serializers.ModelSerializer):
    idPatient = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Patient.objects.all(), source='patient')
    idDoctor = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Doctor.objects.all(), source='doctor')
    idNurse = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Nurse.objects.all(), source='nurse')
    idHospital = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Hospital.objects.all(), source='hospital')
    idProcedure = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Procedure.objects.all(), source='procedure')

    class Meta:
        model = Development
        fields = ['date', 'room', 'comment', 'patient', 'idPatient', 'doctor', 'idDoctor', 'nurse', 'idNurse', 'hospital', 'idHospital', 'procedure', 'idProcedure']
        read_only_fields = ['patient', 'doctor', 'nurse', 'hospital', 'procedure']
        depth = 1

    def create(self, validated_data):

        developmentInstance = Development.objects.create(**validated_data)
        return developmentInstance