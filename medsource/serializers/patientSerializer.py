from rest_framework import serializers
from medsource.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    idEps = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Patient.objects.all(), source='hospital')

    class Meta:
        model = Patient
        fields = ['identification', 'date_of_birth', 'phone', 'marital_status', 'blood_type', 'eps', 'idEps']
        read_only_fields = ['eps']
        depth = 1

    def create(self, validated_data):

        patientInstance = Patient.objects.create(**validated_data)
        return patientInstance
    