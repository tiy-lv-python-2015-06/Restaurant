from django.views.generic import DetailView, ListView, CreateView
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


class RestaurantCreate(CreateView):
    model = Restaurant
    fields = ['user', 'business_name', 'email', 'address', 'city',
              'state', 'zip_code', 'phone_number']
    template_name = 'registration/restaurant_registration.html'
    success_url = '/'
