from rest_framework.viewsets import ModelViewSet
from incomings.models import Incoming
from .serializers import IncomingSerializer

class IncomingViewSet(ModelViewSet):
    
    queryset = Incoming.objects.all()
    serializer_class = IncomingSerializer