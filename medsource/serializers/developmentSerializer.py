from rest_framework import serializers
from medsource.models import Development, Patient, Doctor, Nurse, Hospital, Procedure


class DevelopmentSerializer(serializers.ModelSerializer):
    identification_patient = serializers.IntegerField(write_only=True)
    identification_doctor = serializers.IntegerField(write_only=True)
    identification_nurse = serializers.IntegerField(write_only=True)
    id_hospital = serializers.IntegerField(write_only=True)
    id_procedure = serializers.IntegerField(write_only=True)

    class Meta:
        model = Development
        fields = "__all__"
        depth = 1

    def validate(self, data):
        validated_data = dict()
        validated_data["date"] = data["date"]
        validated_data["room"] = data["room"]
        validated_data["comment"] = data["comment"]
        try:
            doctor = Doctor.objects.get(identification=data["identification_doctor"])
            validated_data["doctor"] = doctor
            patient = Patient.objects.get(identification=data["identification_patient"])
            validated_data["patient"] = patient
            nurse = Nurse.objects.get(identification=data["identification_nurse"])
            validated_data["nurse"] = nurse
            procedure = Procedure.objects.get(id=data["id_procedure"])
            validated_data["procedure"] = procedure
            hospital = Hospital.objects.get(id=data["id_hospital"])
            validated_data["hospital"] = hospital
        except:
            raise serializers.ValidationError(f"Invalid data")
        return validated_data

    def create(self, validated_data):
        developmentInstance = Development.objects.create(**validated_data)
        return developmentInstance
