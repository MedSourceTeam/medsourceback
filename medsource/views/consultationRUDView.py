from rest_framework import generics
from medsource.serializers import ConsultationSerializer
from medsource.models import Consultation


class ConsultationRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    lookup_field = "id"
    