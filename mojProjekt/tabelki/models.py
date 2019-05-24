from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=6)