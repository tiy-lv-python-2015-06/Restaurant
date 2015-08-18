from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from restaurant.models import Restaurant, FoodItem


class Customer(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=10, null=True)

    def __str__(self):
        return ("User: {}, Address: {}, City: {}, State: {}, Zipcode: {},"
                "Phone: {}".format(self.user, self.address, self.city,
                                   self.state, self.zip_code, self.phone))


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    customer = models.ForeignKey(Customer)
    timestamp = models.DateTimeField(auto_now_add=True)
    submited = models.BooleanField(default=False)

    def __str__(self):
        return ("Restaurant: {}, Customer: {}, Time: {}".format(
            self.restaurant, self.customer, self.timestamp
        ))


class OrderItem(models.Model):
    fooditem = models.ForeignKey(FoodItem)
    order = models.ForeignKey(Order)
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)], blank=False)
