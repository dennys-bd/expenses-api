from rest_framework import serializers
from shoppings.models import Category, Shopping, Installment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'user',)
        read_only_fields = ('user',)

class ShoppingSerializer(serializers.ModelSerializer):
    inst_price = serializers.DecimalField(decimal_places=2, max_digits=11, required=False, write_only=True)
    inst_number = serializers.IntegerField(required=False, write_only=True)

    class Meta:
        model = Shopping
        fields = (
            'id', 'account', 'card', 'category', 'debt_type',
            'local', 'description', 'date', 'price', 'tags',
            'inst_price', 'inst_number',
        )

class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installment
        fields = (
            'id', 'shopping', 'installment_number', 
            'installments_price', 'due_date'
        )

