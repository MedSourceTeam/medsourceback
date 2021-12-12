from django.db.models import query
from rest_framework.serializers import Serializer
from medsource import serializers
from medsource.models import Consultation
from medsource.serializers import ShowConsultationSerializer
from rest_framework import generics


class ConsultationListView(generics.ListAPIView):
    serializer_class = ShowConsultationSerializer
    queryset = Consultation.objects.all()