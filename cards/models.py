from django.db import models
from django.core.validators import MaxValueValidator
from accounts.models import Account

class Card(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    flag = models.CharField(max_length=25)
    limit = models.DecimalField(max_digits=11, decimal_places=2)
    best_day = models.IntegerField(default=1, validators=[MaxValueValidator(31)])
    due_day = models.IntegerField(default=1, validators=[MaxValueValidator(31)])

    def __str__(self):
        return self.name
