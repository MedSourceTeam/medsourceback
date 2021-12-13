from rest_framework import generics
from medsource.models import Procedure
from medsource.serializers import ProcedureSerializer


class ProcedureListView(generics.ListAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        uvr = self.request.query_params.get('uvr', None)
        queryset = Procedure.objects.all()

        if name:
            queryset = queryset.filter(name__icontains=name)
        if uvr:
            queryset = queryset.filter(uvr__gte=uvr)

        return queryset
