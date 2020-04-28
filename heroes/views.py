from rest_framework.viewsets import ModelViewSet

from .serializers import HeroesSerializer
from .models import Hero


# Create your views here.
class HeroApiViewSet(ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroesSerializer
