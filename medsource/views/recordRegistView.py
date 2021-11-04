from rest_framework import generics
from medsource.serializers import RecordSerializer
from medsource.models import Record


class RecordRegistView(generics.CreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer