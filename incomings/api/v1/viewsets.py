from rest_framework.viewsets import ModelViewSet
from incomings.models import Incoming
from .serializers import IncomingSerializer
from django.db import transaction

class IncomingViewSet(ModelViewSet):
    serializer_class = IncomingSerializer
    filter_fields = ['account', 'account__id']

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @transaction.atomic
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        return Incoming.objects.select_related('account').filter(account__user=self.request.user)
