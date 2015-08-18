from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from restaurant.models import FoodItem


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ('name', 'price', 'description', 'category', )


class RestaurantCreateForm(UserCreationForm):
    """
    Form for Registering new Restaurants
    """
    business_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=30, required=True)
    zip_code = forms.CharField(max_length=10, required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('username', 'business_name', 'address',
                  'city', 'state', 'zip_code', 'phone_number')
