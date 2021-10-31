from rest_framework import serializers
from medsource.models import Hospital


class HospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = '__all__'
