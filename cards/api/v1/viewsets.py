from rest_framework.viewsets import ModelViewSet
from cards.models import Card
from .serializers import CardSerializer

class CardViewSet(ModelViewSet):
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.all()