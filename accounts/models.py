from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Account(models.Model):
    name = models.CharField(max_length=50)
    best_day = models.IntegerField(
        validators=[
            MaxValueValidator(31)
        ]
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=11)

    def __str__(self):
        return self.usuario.name