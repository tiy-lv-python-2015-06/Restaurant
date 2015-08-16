from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from customer.models import Customer
from django.views.generic import ListView, CreateView
from customer.models import Order, OrderItem
from restaurant.forms import UserForm
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


def menu(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    return render(request, "order/menu.html",
                  context={'foods': restaurant.fooditem_set.all(), 'pk': pk})


class PlaceOrder(CreateView):
    model = OrderItem
    fields = ('quantity',)
    success_url = reverse_lazy('menu')
    template_name = "order/order.html"

    def form_valid(self, form):
        form.instance.fooditem = self.request.fooditem
        if self.request.user.order.get(submited=False) is None:
            form.instance.order = self.request.user.order.get(submited=False)
        else:
            form.instance.order = Order(self.request.Restaurant,
                                        self.request.user,)
        return super(PlaceOrder, self).form_valid(form)


class Confirm(ListView):
    model = Order
    template_name = "order/confirm.html"
    context_object_name = 'order'


def createuser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            # user = authenticate(username=None, password=None)
            # login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserForm()

    return render(request, 'registration/customer_registration.html',
                  {'form': form})
