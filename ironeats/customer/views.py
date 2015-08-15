from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from restaurant.models import Restaurant


class Home(ListView):
    model = Restaurant
    template_name = "home.html"
    queryset = Restaurant.objects.all()
    context_object_name = 'restaurant'
    paginate_by = 20