from django.core.urlresolvers import reverse_lazy
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView, CreateView
from customer.models import Customer
from restaurant.models import Restaurant
from django.views.generic import ListView, CreateView
from customer.models import Order, OrderItem
from restaurant.models import Restaurant, FoodItem


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
    
def menu(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    return render(request, "order/menu.html", context={
        'foods': restaurant.fooditem_set.all(), 'pk': pk })

class PlaceOrder(CreateView):
    model = OrderItem
    fields = ('quantity',)
    success_url = reverse_lazy('menu')
    # Default = chirp_form.html
    template_name = "order/order.html"

    def form_valid(self, form):
        form.instance.fooditem = self.request.fooditem
        if self.request.user.order.get(submited = False) == None:
            form.instance.order = self.request.user.order.get(submited = False)
        else:
            form.instance.order = Order(self.request.Restaurant, self.request.user,)
        return super(PlaceOrder, self).form_valid(form)

class Confirm(ListView):
    model = Order
    template_name = "order/confirm.html"
    # queryset = Order.objects.orderitems_set.all()
    context_object_name = 'order'