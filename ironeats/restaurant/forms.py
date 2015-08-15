from django.forms import ModelForm
from django.contrib.auth.models import User
from restaurant.models import Restaurant, FoodItem


class UserForm(ModelForm):
    class Meta:
        model = User, Restaurant
        fields = ('Business Name', 'address', 'city', 'state', 'zipcode',
                  'phone number', 'username', 'password')


class FoodForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ()
