from django.contrib.auth.models import User
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=100)
    user = models.OneToOneField(User)


class FoodItem(models.Model):
    APPETIZER = 'A'
    SOUPSALAD = 'S'
    ENTREE = 'E'
    DESSERT = 'D'
    MENU_CATEGORY_CHOICES = (
        (APPETIZER, 'Appetizers'),
        (SOUPSALAD, 'Soups and Salads'),
        (ENTREE, 'Entrees'),
        (DESSERT, 'Desserts')
    )
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=150)
    category = models.CharField(max_length=2, choices=MENU_CATEGORY_CHOICES,
                                default=ENTREE, verbose_name='Menu Category')
