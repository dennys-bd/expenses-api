from rest_framework import serializers
from shoppings.models import Category, Shopping, Installment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'user',)
        read_only_fields = ('user',)


class InstallmentSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField('desc')

    class Meta:
        model = Installment
        fields = (
            'id', 'shopping', 'installment_number', 
            'installment_price', 'due_date', 'description'
        )

    def desc(self, obj):
        return obj.__str__()



class ShoppingSerializer(serializers.ModelSerializer):
    installments = InstallmentSerializer(source='installment_set', many=True, required=False)
    inst_price = serializers.DecimalField(decimal_places=2, max_digits=11, required=False, write_only=True)
    inst_number = serializers.IntegerField(required=False, write_only=True)

    class Meta:
        model = Shopping
        fields = (
            'id', 'account', 'card', 'category', 'debt_type',
            'local', 'description', 'date', 'price', 'tags',
            'inst_price', 'inst_number', 'installments',
        )
        read_only_fields = ('installments',)
