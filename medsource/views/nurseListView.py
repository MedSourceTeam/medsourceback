from medsource.models import Nurse
from medsource.serializers import ShowNurseSerializer
from rest_framework import generics


class NurseListView(generics.ListAPIView):

    serializer_class = ShowNurseSerializer

    def get_queryset(self):
        identification = self.request.query_params.get('identification', None)
        hospital = self.request.query_params.get('hospital', None)
        area = self.request.query_params.get('area', None)
        queryset = Nurse.objects.all()

        if identification:
            queryset = queryset.filter(identification=identification)
        if hospital:
            queryset = queryset.filter(hospital__name__icontains=hospital)
        if area:
            queryset = queryset.filter(area__icontains=area)

        return queryset