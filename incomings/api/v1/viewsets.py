from rest_framework.viewsets import ModelViewSet
from incomings.models import Incoming
from .serializers import IncomingSerializer

class IncomingViewSet(ModelViewSet):
    serializer_class = IncomingSerializer

    def get_queryset(self):
        return Incoming.objects.all()