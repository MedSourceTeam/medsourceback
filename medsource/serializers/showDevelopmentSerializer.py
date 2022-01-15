from rest_framework import serializers
from medsource.models import Development, Patient, Doctor, Nurse, Hospital, Procedure


class ShowDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Development
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'date': instance.date,
            'room': instance.room,
            'comment': instance.comment if instance.comment != None else '',
            'patient': instance.patient.full_name,
            'doctor': instance.doctor.user.first_name + " " + instance.doctor.user.last_name,
            'nurse': instance.nurse.user.first_name + " " + instance.nurse.user.last_name,
            'hospital': instance.hospital.name,
            'procedure': instance.procedure.name
        }

    def to_internal_value(self, data):
        doctor_names = data.get("doctor").split()
        doctor_first_name = doctor_names[0]
        doctor_last_name = ""
        if len(doctor_names) > 1:
            doctor_last_name = doctor_names[1]
        nurse_names = data.get("nurse").split()
        nurse_first_name = nurse_names[0]
        nurse_last_name = ""
        if len(nurse_names) > 1:
            nurse_last_name = nurse_names[1]
        return {
            "id": data.get(id),
            "date": data.get("date"),
            "comment": data.get("comment"),
            "patient": Patient.objects.get(full_name=data.get("patient")),
            "doctor": Doctor.objects.get(user__first_name=doctor_first_name, user__last_name=doctor_last_name),
            "nurse": Nurse.objects.get(user__first_name=nurse_first_name, user__last_name=nurse_last_name),
            "hospital": Hospital.objects.get(name=data.get("hospital")),
        }
