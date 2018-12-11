from django.db import models
from accounts.models import Account

class Incoming(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    name = models.CharField(max_length=25)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.CharField(max_length=255, null=True, blank=True)
    due_day = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)