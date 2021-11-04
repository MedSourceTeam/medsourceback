from rest_framework import serializers
from medsource.models import Record

class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'

    def create(self, validated_data):

        recordInstance = Record.objects.create(**validated_data)
        return recordInstance
