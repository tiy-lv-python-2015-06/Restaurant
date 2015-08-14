from django.contrib.auth.models import User
from django.db import models
from restaurant.models import Restaurant


class Customer(models.Model):
    user = models.OneToOneField(User)


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    customer = models.ForeignKey(Customer)
    menu = models.ForeignKey(FoodItem)
    timestamp = models.DateTimeField()