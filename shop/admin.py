from django.contrib import admin

# Register your models here.
from shop.models import Products, Customer


admin.site.register(Products)
admin.site.register(Customer)