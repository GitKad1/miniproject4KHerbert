# orderPizza/models.py

from django.db import models
from django.contrib.auth.models import User as DjangoUser
import datetime


class Pizza(models.Model):
    topping = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)

    def __str__(self):
        return f"{self.topping} - ${self.price}"


class UserProfile(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=10, unique=True, blank=True)


    def __str__(self):
        return f"Profile of {self.username}"


class Order(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    topping = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.user.username}'s order ({self.date.date()}): {self.topping} - ${self.price}"