from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=150)
    #category = [selection - relationship status]


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    customer = models.ForeignKey(Customer)
    menu = models.ForeignKey(FoodItem)
    timestamp = models.DateTimeField()


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    user = models.OneToOneField(User)


class Customer(models.Model):
    user = models.OneToOneField(User)
