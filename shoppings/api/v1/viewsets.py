from rest_framework.viewsets import ModelViewSet
from shoppings.models import Category, Shopping, Installment
from .serializers import CategorySerializer, ShoppingSerializer, InstallmentSerializer

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

class ShoppingViewSet(ModelViewSet):
    serializer_class = ShoppingSerializer

    def get_queryset(self):
        return Shopping.objects.all()

class InstallmentViewSet(ModelViewSet):
    serializer_class = InstallmentSerializer

    def get_queryset(self):
        return Installment.objects.all()