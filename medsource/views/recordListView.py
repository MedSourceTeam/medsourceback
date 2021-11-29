from rest_framework import generics
from medsource.models import Record
from medsource.serializers import RecordSerializer


class RecordListView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer