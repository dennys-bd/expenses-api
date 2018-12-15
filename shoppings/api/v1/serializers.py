from rest_framework.serializers import ModelSerializer
from shoppings.models import Category, Shopping, Installment
from dj_database_url import parse as dburl

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'user')

class ShoppingSerializer(ModelSerializer):

    class Meta:
        model = Shopping
        fields = (
            'id', 'account', 'card', 'category', 'debt_type',
            'local', 'description', 'date', 'price', 'tags'
        )

class InstallmentSerializer(ModelSerializer):
    class Meta:
        model = Installment
        fields = (
            'id', 'shopping', 'installment_number', 
            'installments_price', 'due_date'
        )
