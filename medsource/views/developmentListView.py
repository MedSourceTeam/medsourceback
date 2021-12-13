from django.db.models import query
from rest_framework.serializers import Serializer
from medsource import serializers
from medsource.models import Development
from medsource.serializers import ShowDevelopmentSerializer
from rest_framework import generics


class DevelopmentListView(generics.ListAPIView):
    serializer_class = ShowDevelopmentSerializer

    def get_queryset(self):
        patient = self.request.query_params.get('patient', None)
        doctor = self.request.query_params.get('doctor', None)
        nurse = self.request.query_params.get('nurse', None)
        procedure = self.request.query_params.get('procedure', None)
        hospital = self.request.query_params.get('hospital', None)
        date = self.request.query_params.get('date', None)
        queryset = Development.objects.all()

        if patient:
            queryset = queryset.filter(patient__full_name__icontains=patient)
        if doctor:
            queryset = queryset.filter(doctor__identification=doctor)
        if nurse:
            queryset = queryset.filter(nurse__identification=nurse)
        if procedure:
            queryset = queryset.filter(procedure__name__icontains=procedure)
        if hospital:
            queryset = queryset.filter(hospital__name__icontains=hospital)
        if date:
            queryset = queryset.filter(date=date)

        return queryset