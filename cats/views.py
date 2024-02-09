from rest_framework import viewsets 

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class CatDetail(viewsets.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
