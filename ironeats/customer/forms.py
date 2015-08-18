from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerCreationForm(UserCreationForm):
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'address', 'city', 'state', 'zip_code', 'phone')
