from rest_framework import generics
from medsource.models import Record
from medsource.serializers import RecordSerializer


class RecordListView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        kind = self.request.query_params.get('kind', None)
        sort = self.request.query_params.get('sort', None)
        queryset = Record.objects.all()

        if name:
            queryset = queryset.filter(name__icontains=name)
        if kind:
            queryset = queryset.filter(kind__icontains=kind)
        if sort:
            queryset = queryset.filter(sort__icontains=sort)

        return queryset