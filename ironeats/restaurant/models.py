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

    def has_menu(self):
        menu_exists = (FoodItem.objects.get(pk=self.user.restaurant.id) != None)
        return menu_exists

    def get_menu_items(self):
        menu_list = FoodItem.objects.get(pk=self.user.restaurant.id)
        return menu_list

    # def has_rated_movie(self, movie_id):
    #     rater = Rater.objects.get(pk=self.user.rater.id)
    #     ratings = rater.rating_set
    #     rated = len(ratings.filter(movie__id=movie_id)) > 0
    #     return rated

    def __str__(self):
        return ("Name: {}, Address: {}, City: {}, State: {}, Zipcode: {},"
                "Phone: {}, User: {}".format(self.name, self.address, self.city,
                                             self.state, self.zip_code,
                                             self.phone, self.user))


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

    def __str__(self):
        return ("Restaurant: {}, Name: {}, Price: {}, Desc: {}, Category: {}"
                .format(self.restaurant, self.name, self.price,
                        self.description, self.category))
