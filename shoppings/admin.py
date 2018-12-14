from django.contrib import admin
from .models import Category, Shopping, Installment

admin.site.register(Category) 
admin.site.register(Shopping) 
admin.site.register(Installment)