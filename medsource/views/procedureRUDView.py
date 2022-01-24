from rest_framework import generics
from medsource.serializers import ProcedureSerializer
from medsource.models import Procedure


class ProcedureRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
