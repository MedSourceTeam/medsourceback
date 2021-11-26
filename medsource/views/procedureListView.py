from rest_framework import generics
from medsource.models import Procedure
from medsource.serializers import ProcedureSerializer


class ProcedureListView(generics.ListAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
