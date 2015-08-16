
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
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView, CreateView, UpdateView, \
    DeleteView
from customer.models import Order
from restaurant.models import Restaurant, FoodItem



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

class OrderList(DetailView):
    model = Restaurant
    pk_url_kwarg = 'restaurant_id'
    template_name = 'restaurant/order_list.html'


class CreateMenu(CreateView):
    model = FoodItem
    fields = ('name', 'price', 'description', 'category', )
    # success_url = reverse_lazy('manage_menu')
    template_name = "restaurant/create_menu.html"

    def get_success_url(self):
        return reverse('manage_menu',
                       kwargs={'restaurant_id':
                                   self.kwargs.get('restaurant_id', None)})

    def get_context_data(self, **kwargs):
        context = super(CreateMenu, self).get_context_data(**kwargs)
        context['restaurant_id'] = self.kwargs.get('restaurant_id', None)
        return context

    def form_valid(self, form):
        # form.instance.restaurant_id = self.request.user.restaurant.id
        form.instance.restaurant_id = self.kwargs.get('restaurant_id', None)
        # form.instance.movie_id = self.kwargs.get('movie_id', None)
        form.instance.name = form.cleaned_data.get('name', None)
        form.instance.price = form.cleaned_data.get('price', None)
        form.instance.description = form.cleaned_data.get('description', None)
        form.instance.category = form.cleaned_data.get('category', None)
        return super(CreateMenu, self).form_valid(form)


class ManageMenu(ListView):
    model = FoodItem
    template_name = "restaurant/manage_menu.html"
    # paginate_by = 10

    def get_queryset(self):
        queryset = Restaurant.objects.get(
            pk=self.kwargs.get('restaurant_id', None)).fooditem_set.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ManageMenu, self).get_context_data(**kwargs)
        context['restaurant'] = Restaurant.objects.get(
            pk=self.kwargs.get('restaurant_id', None))
        return context


class UpdateMenu(UpdateView):
    model = FoodItem
    fields = ['name', 'price', 'description', 'category', ]
    pk_url_kwarg = 'fooditem_id'
    template_name = "restaurant/update_menu.html"

    def get_success_url(self):
        fooditem = FoodItem.objects.get(pk=self.kwargs.get('fooditem_id', None))
        return reverse('manage_menu',
                       kwargs={'restaurant_id': fooditem.restaurant.id})


class DeleteItem(DeleteView):
    model = FoodItem
    pk_url_kwarg = 'fooditem_id'
    template_name = "restaurant/delete_menu_item.html"

    def get_success_url(self):
        fooditem = FoodItem.objects.get(pk=self.kwargs.get('fooditem_id', None))
        return reverse('manage_menu',
                       kwargs={'restaurant_id': fooditem.restaurant.id})


class DeleteMenu(DeleteView):
    model = FoodItem

