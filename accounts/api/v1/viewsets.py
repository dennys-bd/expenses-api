from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from accounts.models import Account
from .serializers import AccountSerializer

class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def test_detail(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def test(self, request):
        pass