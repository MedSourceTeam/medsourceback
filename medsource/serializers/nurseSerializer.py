from rest_framework import serializers
from medsource.models import Nurse
from django.contrib.auth.models import User

from medsource.models.user import Hospital
from .userSerializer import UserSerializer


class NurseSerializer(serializers.ModelSerializer):
    idHospital = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Hospital.objects.all(), source='hospital')
    user = UserSerializer()

    class Meta:
        model = Nurse
        fields = ['user', 'identification', 'education',
                  'area', 'hospital', 'idHospital']
        read_only_fields = ['hospital']
        depth = 1

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data['user']
        )
        validated_data['user'] = user
        doctorInstance = Nurse.objects.create(**validated_data)
        return doctorInstance
