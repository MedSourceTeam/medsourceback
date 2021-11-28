from rest_framework import serializers
from medsource.models import Consultation, Patient, Doctor, Hospital

class ConsultationSerializer(serializers.ModelSerializer):
    identification_patient = serializers.IntegerField(write_only=True)
    identification_doctor = serializers.IntegerField(write_only=True)
    id_hospital = serializers.IntegerField(write_only=True)

    class Meta:
        model = Consultation
        fields = '__all__'
        depth = 1

    def validate(self, data):
        validated_data = dict()
        validated_data['pulse'] = data['pulse']
        validated_data['height'] = data['height']
        validated_data['weight'] = data['weight']
        validated_data['pa'] = data['pa']
        validated_data['pr'] = data['pr']
        validated_data['t'] = data['t']
        validated_data['medication'] = data['medication']
        validated_data['symptom'] = data['symptom']
        validated_data['diagnosis'] = data['diagnosis']
        try:
            doctor = Doctor.objects.get(identification=data["identification_doctor"])
            validated_data["doctor"] = doctor
            patient = Patient.objects.get(identification=data["identification_patient"])
            validated_data["patient"] = patient
            hospital = Hospital.objects.get(id=data["id_hospital"])
            validated_data["hospital"] = hospital
        except:
            raise serializers.ValidationError(f"Invalid data")
        else:
            return validated_data


    def create(self, validated_data):

        consultationInstance = Consultation.objects.create(**validated_data)
        return consultationInstance