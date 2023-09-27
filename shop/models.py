from django.db import models

# Create your models here.

class Products(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    pictures = models.ImageField(upload_to = 'images', null = True, blank = True)
    order_status = models.BooleanField(default=False)
    items = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length = 100)
    address = models.TextField(blank = True, null = True)
    phone = models.IntegerField(blank = True, null = True)
    def __str__(self):
        return self.name
