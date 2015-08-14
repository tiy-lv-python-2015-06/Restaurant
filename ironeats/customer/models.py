from django.contrib.auth.models import User
from django.db import models
from restaurant.models import Restaurant, FoodItem


class Customer(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    customer = models.ForeignKey(Customer)
    fooditem = models.ForeignKey(FoodItem)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("Restaurant: {}, Customer: {}, FoodItem: {}, Time: {}".format(
            self.restaurant, self.customer, self.fooditem, self.timestamp
        ))