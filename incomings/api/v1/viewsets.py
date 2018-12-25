from rest_framework.viewsets import ModelViewSet
from incomings.models import Incoming
from .serializers import IncomingSerializer

class IncomingViewSet(ModelViewSet):
    serializer_class = IncomingSerializer
    filter_fields = ['account', 'account__id']

    def get_queryset(self):
        return Incoming.objects.select_related('account').filter(account__user=self.request.user)

        # Room.objects.select_related('house').filter(house__street=xyz)