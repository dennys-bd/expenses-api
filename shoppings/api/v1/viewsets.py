from rest_framework.viewsets import ModelViewSet
from shoppings.models import Category, Shopping, Installment
from .serializers import InstallmentSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer

class ShoppingViewSet(ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer

class InstallmentViewSet(ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer