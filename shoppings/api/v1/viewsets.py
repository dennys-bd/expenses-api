from rest_framework.viewsets import ModelViewSet
from shoppings.models import Category, Shopping, Installment
from .serializers import CategorySerializer, ShoppingSerializer, InstallmentSerializer
from django.db import transaction

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class ShoppingViewSet(ModelViewSet):
    serializer_class = ShoppingSerializer

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
        return Shopping.objects.all()

class InstallmentViewSet(ModelViewSet):
    serializer_class = InstallmentSerializer

    def get_queryset(self):
        return Installment.objects.all()