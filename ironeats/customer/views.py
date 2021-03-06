from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from customer.forms import CustomerCreationForm
from customer.models import Customer
from django.views.generic import ListView, CreateView
from customer.models import Order, OrderItem
from restaurant.models import Restaurant, FoodItem


class Home(ListView):
    model = Restaurant
    template_name = "home.html"
    queryset = Restaurant.objects.all()
    context_object_name = 'restaurant'
    paginate_by = 10


def menu(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    current_order = []
    try:
        for item in request.user.customer.order_set.get(submited=False).orderitem_set.all():
            current_order.append(item)
    except:
        current_order = []
    return render(request, "order/menu.html",
                  context={'foods': restaurant.fooditem_set.all(),
                           'pk': pk, 'current_order': current_order})


class PlaceOrder(CreateView):
    model = OrderItem
    fields = ('quantity',)
    template_name = "order/order.html"

    def get_success_url(self):
        return reverse('menu', kwargs={'pk': self.kwargs.get('pk', None)})

    def get_context_data(self, **kwargs):
        context = super(PlaceOrder, self).get_context_data(**kwargs)
        fooditem = self.kwargs.get('pk')
        context['restaurant'] = FoodItem.objects.get(pk=fooditem).restaurant
        context['fooditem'] = FoodItem.objects.get(pk=fooditem)
        return context

    def form_valid(self, form):
        fooditem = FoodItem.objects.get(pk=self.request.POST.get('fooditempk'))
        form.instance.fooditem = fooditem
        try:
            order = self.request.user.customer.order_set.get(submited=False)
            form.instance.order = order
            form.instance.order.save()
        except:
            form.instance.order = Order.objects.create(
                restaurant=fooditem.restaurant,
                customer=self.request.user.customer, )
            form.instance.order.save()
        return super(PlaceOrder, self).form_valid(form)


class Confirm(ListView):
    model = Order
    template_name = "order/confirm.html"
    context_object_name = 'orders'

    def get_queryset(self):
        current_order = []
        try:
            for item in self.request.user.customer.order_set.get(submited=False).orderitem_set.all():
                current_order.append(item)
            order = self.request.user.customer.order_set.get(submited=False)
            order.submited = True
            order.save()
        except:
            current_order = None
        queryset = current_order
        return queryset


def createuser(request):
    if request.method == "POST":
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = form.save()
            customer = Customer()
            customer.user = user
            customer.address = data['address']
            customer.city = data['city']
            customer.state = data['state']
            customer.zip_code = data['zip_code']
            customer.phone = data['phone']
            customer.save()
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password1'])
            login(request, user)

            return HttpResponseRedirect(reverse('home'))
    else:
        form = CustomerCreationForm()

    return render(request, 'registration/customer_registration.html',
                  {'form': form})
