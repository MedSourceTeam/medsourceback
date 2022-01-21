from medsource.models import Record
from medsource.serializers import RecordSerializer
from rest_framework import generics


class RecordRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
