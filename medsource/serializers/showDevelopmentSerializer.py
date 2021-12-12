from rest_framework import serializers
from medsource.models import Development

class ShowDevelopmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Development
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'date' : instance.date,
            'room' : instance.room,
            'comment' : instance.comment if instance.comment != None else '',
            'patient' : instance.patient.full_name,
            'doctor' : instance.doctor.user.first_name + " " + instance.doctor.user.last_name,
            'nurse' : instance.nurse.user.first_name + " " + instance.nurse.user.last_name,
            'hospital' : instance.hospital.name,
            'procedure' : instance.procedure.name
        }