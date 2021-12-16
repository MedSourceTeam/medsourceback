from medsource.models import Doctor
from medsource.serializers import ShowDoctorSerializer
from rest_framework import generics


class DoctorListView(generics.ListAPIView):

    serializer_class = ShowDoctorSerializer

    def get_queryset(self):
        identification = self.request.query_params.get('identification', None)
        hospital = self.request.query_params.get('hospital', None)
        specialization = self.request.query_params.get('specialization', None)
        queryset = Doctor.objects.all()

        if identification:
            queryset = queryset.filter(identification=identification)
        if hospital:
            queryset = queryset.filter(hospital__name__icontains=hospital)
        if specialization:
            queryset = queryset.filter(specialization__icontains=specialization)

        return queryset