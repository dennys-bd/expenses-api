from django.db import models
from accounts.models import Account
from django.dispatch import receiver

class Incoming(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    name = models.CharField(max_length=25)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.CharField(max_length=255, null=True, blank=True)
    due_day = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

@receiver(models.signals.pre_save, sender=Incoming)
def incoming_pre_save(sender, instance, *args, **kwargs):
    if instance.id is not None:
        incoming = Incoming.objects.get(pk=instance.id)
        instance.account.balance -= incoming.value
        instance.account.save()        
        
@receiver(models.signals.post_save, sender=Incoming)
def incoming_post_save(sender, instance, created, *args, **kwargs):
    instance.account.balance += instance.value
    instance.account.save()

@receiver(models.signals.pre_delete, sender=Incoming)
def incomming_pre_delete(sender, instance, *args, **kwargs):
    instance.account.balance -= instance.value
    instance.account.save()