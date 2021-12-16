from django.db import models

class Produs(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    total = models.CharField(max_length=200)
