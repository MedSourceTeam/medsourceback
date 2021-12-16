from django.db.models import query
from rest_framework.serializers import Serializer
from medsource import serializers
from medsource.models import Consultation
from medsource.serializers import ShowConsultationSerializer
from rest_framework import generics


class ConsultationListView(generics.ListAPIView):
    serializer_class = ShowConsultationSerializer

    def get_queryset(self):
        patient = self.request.query_params.get('patient', None)
        hospital = self.request.query_params.get('hospital', None)
        doctor = self.request.query_params.get('doctor', None)
        queryset = Consultation.objects.all()

        if patient:
            queryset = queryset.filter(patient__full_name__icontains=patient)
        if hospital:
            queryset = queryset.filter(hospital__name__icontains=hospital)
        if doctor:
            queryset = queryset.filter(doctor__identification=doctor)

        return queryset