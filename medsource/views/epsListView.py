from rest_framework import generics
from medsource.models import Eps
from medsource.serializers import EpsSerializer


class EpsListView(generics.ListAPIView):
    queryset = Eps.objects.all()
    serializer_class = EpsSerializer