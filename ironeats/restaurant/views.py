from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView
from customer.models import Order
from restaurant.models import Restaurant


class RestaurantProfile(DetailView):
    model = Restaurant
    pk_url_kwarg = 'restaurant_id'
    template_name = 'restaurant/restaurant_profile.html'


class OrderList(ListView):
    model = Order
    template_name = "restaurant/order_list.html"
    queryset = Order.objects.all().order_by('timestamp')
    paginate_by = 20

