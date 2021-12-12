from rest_framework import serializers
from medsource.models import Consultation

class ShowConsultationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consultation
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'patient' : instance.patient.full_name,
            'doctor' : instance.doctor.user.first_name + ' ' + instance.doctor.user.last_name,
            'hospital' : instance.hospital.name,
            'pulse' : instance.pulse,
            'height' : instance.height,
            'weight' : instance.weight,
            'pa' : instance.pa,
            'pr' : instance.pr,
            't' : instance.t,
            'medication' : instance.medication,
            'symptom' : instance.symptom,
            'diagnosis' : instance.diagnosis
        }