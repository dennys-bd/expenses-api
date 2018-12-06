from django.db import models
from accounts.models import Account
from cards.models import Card

class Shopping(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True)
    local = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    full_price = models.DecimalField(decimal_places=2, max_digits=11)
    has_installments = models.BooleanField(default=False)
    installments_number = models.IntegerField(null=True, blank=True)
    installments_price = models.DecimalField(decimal_places=2, max_digits=11, null=True, blank=True)
    tags = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)