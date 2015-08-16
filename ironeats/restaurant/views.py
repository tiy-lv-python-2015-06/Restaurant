from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView, CreateView
from customer.models import Order
from restaurant.forms import UserForm
from restaurant.models import Restaurant
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect


class RestaurantProfile(DetailView):
    model = Restaurant
    pk_url_kwarg = 'restaurant_id'
    template_name = 'restaurant/restaurant_profile.html'


class OrderList(ListView):
    model = Order
    template_name = "restaurant/order_list.html"
    queryset = Order.objects.all().order_by('timestamp')
    paginate_by = 20


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


class RestaurantCreate(CreateView):
    model = Restaurant
    fields = ['user', 'business_name', 'email', 'address', 'city',
              'state', 'zip_code', 'phone_number']
    template_name = 'registration/restaurant_registration.html'
    success_url = '/'
#
#     def form_valid(self, form):
#         self.object = form.save()
#         return super(RestaurantCreate, self).form_valid(form)

# def restaurantregister(request):
#     if request.method == 'POST':
#         form = RestaurantCreateForm(request.POST)
#
#         if form.is_valid():
#             rest_user = RestaurantCreateForm(request.POST)
#             rest_user.save()
#             return render_to_response('restaurant/restaurant_profile.html')
#     else:
#         form = RestaurantCreateForm()
#     return render_to_response('registration/restaurant_registration.html',
#                               {'form': form},
#                               context_instance=RequestContext(request))
