from rest_framework import serializers
from medsource.models import Procedure


class ProcedureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Procedure
        fields = '__all__'

    def create(self, validated_data):

        procedureInstance = Procedure.objects.create(**validated_data)
        return procedureInstance
