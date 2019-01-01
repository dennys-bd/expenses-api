from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from accounts.models import Account
from .serializers import AccountSerializer, UserSerializer, ExtractSerializer

class CreateOnly(BasePermission):
    """
    create_only
    """
    def has_permission(self, request, view):
            if view.action == 'create':
                return True
            else:
                return IsAuthenticated.has_permission(self, request, view)

class AccountViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'extract':
            return ExtractSerializer
        return AccountSerializer

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    @action(methods=['get'], detail=True)
    def extract(self, request, pk=None):
        account = get_object_or_404(self.get_queryset(), pk=pk)
        account.month = int(request.query_params.get('month'))
        account.year = int(request.query_params.get('year'))
        serializer = self.get_serializer_class()(account)
        return Response(serializer.data)
        
        # else:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # month = request.query_params.get('month')
        # return super().retrieve(request)

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)

    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)

    # @action(methods=['get'], detail=True)
    # def test_detail(self, request, pk=None):
    #     pass

    # @action(methods=['get'], detail=False)
    # def test(self, request):
    #     pass

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (CreateOnly,)

    def get_queryset(self):
        return User.objects.all()



