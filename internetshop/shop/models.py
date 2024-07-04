from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    descript = models.TextField()
    price = models.IntegerField()
    image_url = models.CharField(max_length=256)

    weight = models.IntegerField(null=True, blank=True)
    model = models.CharField(max_length=64, null=True, blank=True)
    processor = models.CharField(max_length=32, null=True, blank=True)
    ram_size = models.IntegerField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    battery_capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    author = models.CharField(max_length=256)
    number = models.IntegerField()
    text = models.TextField()
