from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from restaurant.models import Restaurant, FoodItem


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')





# class RestaurantForm(forms.ModelForm):
#     class Meta:
#         model = Restaurant
#         fields = '__all__'
        # template_name = 'registration/restaurant_registration.html'



# class RestaurantCreateForm(UserCreationForm):
#     """
#     Form for Registering new Restaurants
#     """
#     business_name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(required=True)
#     address = forms.CharField(max_length=100, required=True)
#     city = forms.CharField(max_length=100, required=True)
#     state = forms.CharField(max_length=30, required=True)
#     zip_code = forms.CharField(max_length=10, required=True)
#     phone_number = forms.CharField(max_length=15, required=True)
#
#     class Meta:
#         model = User
#         fields = ('business_name', 'address', 'city', 'state', 'zip_code',
#                   'phone_number', 'username', 'password')
#
#     def save(self, commit=True):
#         user = super(RestaurantCreateForm, self).save(commit=False)
#         user.business_name = self.cleaned_data['business_name']
#         user.email = self.cleaned_data['email']
#         user.address = self.cleaned_data['address']
#         user.city = self.cleaned_data['city']
#         user.state = self.cleaned_data['state']
#         user.zip_code = self.cleaned_data['zip_code']
#         user.phone_number = self.cleaned_datad['phone_number']
#         if commit:
#             user.save()
#         return user
