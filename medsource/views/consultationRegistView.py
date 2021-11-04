from rest_framework import generics
from medsource.serializers import ConsultationSerializer
from medsource.models import Consultation


class ConsultationRegistView(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer