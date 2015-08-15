from django.forms import ModelForm
from restaurant.models import Restaurant, FoodItem


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ()


class FoodForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ()
