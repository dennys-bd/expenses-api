from rest_framework.serializers import ModelSerializer
from cards.models import Card


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', 'flag', 'account')