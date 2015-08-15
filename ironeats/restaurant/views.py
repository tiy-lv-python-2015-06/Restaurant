from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView
from customer.models import Order
from restaurant.forms import RestaurantCreateForm
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


def restaurantregister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'],
                                            form.cleaned_data['business_name'])
            user.save()
            return render_to_response('restaurant/restaurant_profile.html')
    else:
        form = UserCreationForm()
    return render_to_response('registration/restaurant_registration.html',
                              {'form': form},
                              context_instance=RequestContext(request))
