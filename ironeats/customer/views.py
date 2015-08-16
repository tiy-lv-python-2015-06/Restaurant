from django.core.urlresolvers import reverse_lazy, reverse
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView
from customer.models import Order, OrderItem
from restaurant.models import Restaurant, FoodItem


class Home(ListView):
    model = Restaurant
    template_name = "home.html"
    queryset = Restaurant.objects.all()
    context_object_name = 'restaurant'
    paginate_by = 20

def menu(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    return render(request, "order/menu.html", context={
        'foods': restaurant.fooditem_set.all(), 'pk': pk })

class PlaceOrder(CreateView):
    model = OrderItem
    fields = ('quantity',)
    # success_url = reverse_lazy('menu', kwargs= {'pk': OrderItem.order.restaurant.pk})
    template_name = "order/order.html"
    def get_success_url(self):
        return reverse('menu', kwargs={'pk': self.kwags.get('pk', None)})

    def get_context_data(self, **kwargs):
        context = super(PlaceOrder, self).get_context_data(**kwargs)
        fooditem = self.kwargs.get('pk')
        context['restaurant'] = FoodItem.objects.get(pk=fooditem).restaurant
        context['fooditem'] =  FoodItem.objects.get(pk=fooditem)
        return context

    def form_valid(self, form):
        fooditem = FoodItem.objects.get(pk=self.request.POST.get('fooditempk'))
        form.instance.fooditem = fooditem
        if self.request.user.customer.order.get(submited = False) == None:
            form.instance.order = self.request.user.order.get(submited = False)
        else:
            form.instance.order = Order(self.request.Restaurant, self.request.user,)
        return super(PlaceOrder, self).form_valid(form)

class Confirm(ListView):
    model = Order
    template_name = "order/confirm.html"
    # queryset = Order.objects.orderitems_set.all()
    context_object_name = 'order'

