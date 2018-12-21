from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from django.contrib.auth.models import User
from accounts.models import Account

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', 'balance')

class UserSerializer(ModelSerializer):
    accounts = AccountSerializer(source='account_set', many=True)

    class Meta:
        model = User
        # fields = ('id', 'username')
        fields = ('id', 'username', 'accounts')