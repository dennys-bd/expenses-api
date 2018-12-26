from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from datetime import datetime
import shoppings

class Account(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=11)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def monthly_shopping(self, month = datetime.now().month, year = datetime.now().year):
        due_date = f"{year}-{month}-{self.best_day}"
        previous_date = f"{year}-{month}-{self.best_day}"

        return self.shopping_set.filter(date__range=[previous_date, due_date], installment=None),
        shoppings.models.Installment.objects.select_related('shopping').filter(shopping__account=self, date__range=[previous_date, due_date])