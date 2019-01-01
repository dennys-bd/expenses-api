from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Account
from shoppings.api.v1.serializers import ShoppingSerializer, InstallmentSerializer

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(write_only=True)
    class Meta:
        model = Account
        fields = ('id', 'name', 'balance', 'user')

# TODO: Make Month and year come from the serializer to the model
class ExtractSerializer(serializers.ModelSerializer):
    shoppings = ShoppingSerializer(source='monthly_shopping', many=True)
    installments = InstallmentSerializer(source='monthly_installments', many=True)
    # month = serializers.IntegerField(write_only=True)
    # year = serializers.IntegerField(write_only=True)
    class Meta:
        model = Account
        fields = ('id', 'name', 'balance', 'user', 'shoppings', 'installments', 'month', 'year')

class UserSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(source='account_set', many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'accounts')