from rest_framework.serializers import ModelSerializer
from incomings.models import Incoming

class IncomingSerializer(ModelSerializer):
    class Meta:
        model = Incoming
        fields = ('id', 'name', 'value')