from medsource.models import Patient
from medsource.serializers import PatientSerializer
from rest_framework import generics


class PatientListView(generics.ListAPIView):

    serializer_class = PatientSerializer

    def get_queryset(self):
        identification = self.request.query_params.get('identification', None)
        full_name = self.request.query_params.get('full_name', None)
        date_of_birth = self.request.query_params.get('date_of_birth', None)
        eps_name = self.request.query_params.get('eps_name', None)
        queryset = Patient.objects.all()

        if identification:
            queryset = queryset.filter(identification__contains=identification)
        if full_name:
            queryset = queryset.filter(full_name__icontains=full_name) # icontains for case insensitive
        if date_of_birth:
            queryset = queryset.filter(date_of_birth=date_of_birth)
        if eps_name:
            queryset = queryset.filter(eps__name__icontains=eps_name)

        return queryset