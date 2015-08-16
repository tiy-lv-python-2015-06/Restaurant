from django.core.urlresolvers import reverse_lazy, reverse
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView
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
    # Default = chirp_form.html
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
        try:
            order = self.request.user.customer.order.get(submited = False)
            form.instance.order = order
            form.instance.order.save()
        except:
            form.instance.order = Order.objects.create(restaurant=fooditem.restaurant, customer=self.request.user.customer,)
            form.instance.order.save()
        return super(PlaceOrder, self).form_valid(form)


class Confirm(ListView):
    model = Order
    template_name = "order/confirm.html"
    # queryset = Order.objects.orderitems_set.all()
    context_object_name = 'order'

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
