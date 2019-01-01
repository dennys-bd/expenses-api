from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Account(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=11)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    _month = None
    _year = None    

    def __str__(self):
        return self.name

    @property
    def month(self):
        return self._month
    @month.setter
    def month(self, value):
        self._month = value

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def monthly_shopping(self):
        return self.card_set.first().monthly_shopping(self.month, self.year)


    @property
    def monthly_installments(self):
        return self.card_set.first().monthly_installments(self.month, self.year)