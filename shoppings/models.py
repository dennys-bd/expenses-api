from django.db import models
from accounts.models import Account
from cards.models import Card

class Category(models.Model):
    name = models.CharField(max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shopping(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    SHOPPING = 0
    LOAN = 1
    HOME_EXPENSES = 2
    DEBT_TYPE_CHOICES = (
        (SHOPPING, 'Shopping'),
        (LOAN, 'Loan'),
        (HOME_EXPENSES, 'HomeExpenses'),
    )

    debt_type = models.IntegerField(default=0, choices=DEBT_TYPE_CHOICES)

    local = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    description = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=11)
    tags = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Installment(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE)
    installment_number = models.IntegerField(null=True, blank=True)
    installments_price = models.DecimalField(decimal_places=2, max_digits=11)
    due_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['installment_number']
        unique_together = ['shopping', 'installment_number']
        
    def __str__(self):
        return f'{self.shopping.description} {self.installment_number}/{self.shopping.installment_set.count()}'