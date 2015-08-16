from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from customer.models import Customer
from restaurant.models import Restaurant


class Home(ListView):
    model = Restaurant
    template_name = "home.html"
    queryset = Restaurant.objects.all()
    context_object_name = 'restaurant'
    paginate_by = 20


class CustomerCreate(CreateView):
    model = Customer
    fields = ['user', 'address', 'city',
              'state', 'zip_code', 'phone']
    template_name = 'registration/customer_registration.html'
    success_url = '/'