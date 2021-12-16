from rest_framework import serializers
from medsource.models import Doctor

class ShowDoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'identification': instance.identification,
            'full_name' : instance.user.first_name + ' ' + instance.user.last_name,
            'hospital' : instance.hospital.name,
            'specialization' : instance.specialization
        }