from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(write_only=True)
    class Meta:
        model = Account
        fields = ('id', 'name', 'balance', 'user')

class UserSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(source='account_set', many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'accounts')