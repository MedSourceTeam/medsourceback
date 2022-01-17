from cgitb import lookup
from django.db.models import query
from rest_framework.serializers import Serializer
from medsource import serializers
from medsource.models import Development
from medsource.serializers import ShowDevelopmentSerializer
from rest_framework import generics


class DevelopmentRUDView(generics.RetrieveUpdateAPIView):
    serializer_class = ShowDevelopmentSerializer
    queryset = Development.objects.filter()
    lookup_field = "id"

    def perform_update(self, serializer):
        instance = serializer.save()
