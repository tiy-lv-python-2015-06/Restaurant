from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView
from restaurant.models import Restaurant


class RestaurantProfile(ListView):
    model = Restaurant
    template_name = "restaurant/restaurant_profile.html"
    #queryset = Restaurant.objects.get(pk=1)

