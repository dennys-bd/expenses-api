from django.db import models
from django.core.validators import MaxValueValidator
from accounts.models import Account
from datetime import datetime
import shoppings

class Card(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    name = models.CharField(max_length=25)
    flag = models.CharField(max_length=25)
    limit = models.DecimalField(max_digits=11, decimal_places=2)
    best_day = models.IntegerField(default=1, validators=[MaxValueValidator(31)])
    due_day = models.IntegerField(default=1, validators=[MaxValueValidator(31)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def monthly_shopping(self, month = datetime.now().month, year = datetime.now().year):
        due_date = f"{year}-{month}-{self.best_day}"
        previous_date = f"{year}-{month}-{self.best_day}"
        return self.shopping_set.in_date_range(previous_date, due_date).without_installments()

    @property
    def monthly_installments(self, month = datetime.now().month, year = datetime.now().year):
        due_date = f"{year}-{month}-{self.best_day}"
        previous_date = f"{year}-{month}-{self.best_day}"
        return shoppings.models.Installment.objects.by_card(self).in_date_range(previous_date, due_date)