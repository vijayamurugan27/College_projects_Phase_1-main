from django.db import models

# Create your models here.
class PhotoGraphy(models.Model):
    Services = (
        ('Wedding', 'Wedding'),
        ('Ear-Boring', 'Ear-Boring'),
        ('BirthDay', 'BirthDay'),
        ('PhotoShoot', 'PhotoShoot'),
        ('Celebrations', 'Celebrations'),
        ('Others', 'Others'),
        
    )
    name = models.CharField(max_length=60)
    address = models.TextField()
    phone = models.IntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    service = models.CharField(max_length=50, choices=Services)
    pictures = models.ImageField(upload_to = 'images', null = True, blank = True)
    def __str__(self):
        return self.name


