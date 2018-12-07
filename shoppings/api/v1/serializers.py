from rest_framework.serializers import ModelSerializer
from shoppings.models import Category, Shopping, Installment

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ShoppingSerializer(ModelSerializer):
    class Meta:
        model = Shopping
        fields = ('id', 'local', 'description', 'category')

class InstallmentSerializer(ModelSerializer):
    class Meta:
        model = Installment
        fields = ('id', '__str__')