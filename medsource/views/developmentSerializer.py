from rest_framework import generics
from medsource.serializers import DevelopmentSerializer
from medsource.models import Development


class DevelopmentRegistView(generics.CreateAPIView):
    queryset = Development.objects.all()
    serializer_class = DevelopmentSerializer