from django.db import models

# Create your models here.
from django . db import models
class Product(models.Model):
    name = models.CharField(max_length=120)
    descript = models.CharField(max_length=128)
    price = models.IntegerField()
    image_url = models.CharField(max_length=256)