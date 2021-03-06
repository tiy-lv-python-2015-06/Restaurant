from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Restaurant(models.Model):
    business_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=100)
    user = models.OneToOneField(User)

    def has_menu(self):
        menu_exists = (self.user.restaurant.fooditem_set.count() > 0)
        return menu_exists

    def get_menu_items(self):
        menu_list = FoodItem.objects.get(pk=self.user.restaurant.id)
        return menu_list

    def __str__(self):
        return ("Name: {}, Address: {}, City: {}, State: {}, Zipcode: {},"
                "Phone: {}, User: {}".format(self.business_name, self.address,
                                             self.city,
                                             self.state, self.zip_code,
                                             self.phone_number, self.user))


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
    price = models.FloatField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=150)
    category = models.CharField(max_length=2, choices=MENU_CATEGORY_CHOICES,
                                default=ENTREE, verbose_name='Menu Category')

    def __str__(self):
        return ("Name: {}"
                .format(self.name,))
