from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    like = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass