from django.db.models import query
from rest_framework.serializers import Serializer
from medsource import serializers
from medsource.models import Development
from medsource.serializers import ShowDevelopmentSerializer
from rest_framework import generics


class DevelopmentListView(generics.ListAPIView):
    serializer_class = ShowDevelopmentSerializer
    queryset = Development.objects.all()