from accounts.models import Account
from cards.models import Card
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.db import models
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

@receiver(models.signals.pre_save, sender=Category)
def category_before_save(sender, instance, *args, **kwargs):
    instance.name = instance.name.lower()

class ShoppingQuerySet(models.QuerySet):
    def in_date_range(self, previous_date, due_date):
        return self.filter(date__range=[previous_date, due_date])

    def by_card(self, card):
        return self.filter(card=card)

    def by_account(self, account):
        return self.filter(account=account)

    def without_installments(self):
        return self.filter(installment=None)


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

    objects = models.Manager.from_queryset(ShoppingQuerySet)()

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

@receiver(models.signals.pre_save, sender=Shopping)
def shopping_pre_save(sender, instance, *args, **kwargs):
    if instance.id is not None and instance.inst_number is None:
        shopping = Shopping.objects.get(pk=instance.id)
        instance.account.balance += shopping.price
        instance.account.save()

                 
@receiver(models.signals.post_save, sender=Shopping)
def shopping_post_save(sender, instance, created, *args, **kwargs):
    if created and instance.inst_number is not None:
        due_date = instance.date
        for i in range(instance.inst_number):
            instance.installment_set.create(due_date=due_date,
                installment_number=i+1, installment_price=(
                    instance.inst_price or instance.price/instance.inst_number
                )
            )
            due_date += relativedelta(months=1)
    elif instance.inst_number is None:
        instance.account.balance -= instance.price
        instance.account.save()

@receiver(models.signals.pre_delete, sender=Shopping)
def shopping_pre_delete(sender, instance, *args, **kwargs):
    instance.account.balance += instance.price
    instance.account.save()

class InstallmentQuerySet(models.QuerySet):
    def in_date_range(self, previous_date, due_date):
        return self.filter(due_date__range=[previous_date, due_date])

    def by_card(self, card):
        return self.filter(shopping__card=card)

    def by_account(self, account):
        return self.filter(shopping__account=account)

class Installment(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE)
    installment_number = models.IntegerField(null=True, blank=True)
    installment_price = models.DecimalField(decimal_places=2, max_digits=11)
    due_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager.from_queryset(InstallmentQuerySet)()

    @property
    def card(self):
        return self.shopping.card
    
    class Meta:
        ordering = ['installment_number']
        unique_together = ['shopping', 'installment_number']
        
    def __str__(self):
        return f'{self.shopping.description} {self.installment_number}/{self.shopping.installment_set.count()}'

