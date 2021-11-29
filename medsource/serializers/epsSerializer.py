from rest_framework import serializers
from medsource.models import Eps


class EpsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Eps
        fields = '__all__'