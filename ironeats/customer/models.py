from django.contrib.auth.models import User
from django.db import models
from restaurant.models import Restaurant, FoodItem


class Customer(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return ("User: {}, Address: {}, City: {}, State: {}, Zipcode: {},"
                "Phone: {}".format(self.user, self.address, self.city,
                                   self.state, self.zip_code, self.phone))


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    customer = models.ForeignKey(Customer)
    fooditem = models.ForeignKey(FoodItem)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("Restaurant: {}, Customer: {}, FoodItem: {}, Time: {}".format(
            self.restaurant, self.customer, self.fooditem, self.timestamp
        ))
