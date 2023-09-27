from django.db import models

# Create your models here.
class Foods(models.Model):
    FoodChoices = (
        ('Veg', 'Vegetarian'),
        ('Non-Veg', 'Non-veg'),
        ('Vegan', 'Vegan'),
    )
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    FoodChoice = models.CharField(max_length=10, choices=FoodChoices)
    pictures = models.ImageField(upload_to = 'images', null = True, blank = True)
    order_status = models.BooleanField(default=False)
    items = models.IntegerField(default=0)


    def __str__(self):
        return self.name



