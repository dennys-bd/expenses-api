from accounts.models import Account
from cards.models import Card
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'name',)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Category)
def category_before_save(sender, instance, *args, **kwargs):
    instance.name = instance.name.lower()

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
    description = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=11)
    tags = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    _inst_price = None
    _inst_number = None

    def __str__(self):
        return self.description
    
    @property
    def inst_price(self):
        return self._inst_price
    @inst_price.setter
    def inst_price(self, value):
        self._inst_price = value

    @property
    def inst_number(self):
        return self._inst_number
    @inst_number.setter
    def inst_number(self, value):
        self._inst_number = value

    # TODO: Fix the due_date montly's improvement
    def create_installments(self):
        due_date = self.date
        for i in range(self._inst_number):
            Installment.objects.create(shopping=self, due_date=due_date,
                installment_number=i+1, installment_price=(
                    self.inst_price or self.price/self._inst_number
                ))
                 
# TODO: Make sure that it occours under a transaction
# to rollback if installmentes are not created
@receiver(models.signals.post_save, sender=Shopping)
def shopping_post_save(sender, instance, created, *args, **kwargs):
    if created and instance.inst_number is not None:
        instance.create_installments()
        

class Installment(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE)
    installment_number = models.IntegerField(null=True, blank=True)
    installment_price = models.DecimalField(decimal_places=2, max_digits=11)
    due_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['installment_number']
        unique_together = ['shopping', 'installment_number']
        
    def __str__(self):
        return f'{self.shopping.description} {self.installment_number}/{self.shopping.installment_set.count()}'