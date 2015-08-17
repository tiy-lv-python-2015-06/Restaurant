from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, \
    CreateView, UpdateView, DeleteView
from restaurant.forms import RestaurantCreateForm
from restaurant.models import Restaurant, FoodItem


class RestaurantProfile(DetailView):
    model = Restaurant
    pk_url_kwarg = 'restaurant_id'
    template_name = 'restaurant/restaurant_profile.html'

class OrderList(DetailView):
    model = Restaurant
    pk_url_kwarg = 'restaurant_id'
    template_name = 'restaurant/order_list.html'


def login_redirect(request):
    user =  request.user
    if hasattr(user, 'restaurant') and user.restaurant.id > 0:
        return HttpResponseRedirect(reverse('restaurant_profile',
                                            args=[user.restaurant.id]))
    else:
        return HttpResponseRedirect(reverse('home'))


class RestaurantCreate(CreateView):
    model = Restaurant
    fields = ['business_name', 'email', 'address', 'city',
              'state', 'zip_code', 'phone_number']
    template_name = 'registration/restaurant_registration.html'


    def get_success_url(self):
       return reverse('restaurant/restaurant_profile/',
                      kwargs={'restaurant':
                             self.kwargs.get('restaurant_id', None)})

    def form_valid(self, form):
        restaurant = form.save(commit=False)
        restaurant.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RestaurantCreate, self).get_context_data(**kwargs)
        context['user'] = self.request.user.restaurant.id
        return context


def createrest(request):
    if request.method == 'POST':
        form = RestaurantCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = form.save()
            restaurant = Restaurant()
            restaurant.user = user
            restaurant.business_name = data['business_name']
            restaurant.address = data['address']
            restaurant.city = data['city']
            restaurant.state = data['state']
            restaurant.zip_code = data['zip_code']
            restaurant.phone_number = data['phone_number']
            restaurant.save()
            user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, user)

            return HttpResponseRedirect(reverse('restaurant_profile',
                                                args=[user.restaurant.id]))

    else:
        form = RestaurantCreateForm()

    return render(request, 'registration/restaurant_registration.html',
                  {'form': form})



class CreateMenu(CreateView):
    model = FoodItem
    fields = ('name', 'price', 'description', 'category', )
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
        form.instance.restaurant_id = self.kwargs.get('restaurant_id', None)
        form.instance.name = form.cleaned_data.get('name', None)
        form.instance.price = form.cleaned_data.get('price', None)
        form.instance.description = form.cleaned_data.get('description', None)
        form.instance.category = form.cleaned_data.get('category', None)
        return super(CreateMenu, self).form_valid(form)


class ManageMenu(ListView):
    model = FoodItem
    template_name = "restaurant/manage_menu.html"

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
        fooditem = FoodItem.objects.get\
            (pk=self.kwargs.get('fooditem_id', None))
        return reverse('manage_menu',
                       kwargs={'restaurant_id': fooditem.restaurant.id})


class DeleteItem(DeleteView):
    model = FoodItem
    pk_url_kwarg = 'fooditem_id'
    template_name = "restaurant/delete_menu_item.html"

    def get_success_url(self):
        fooditem = FoodItem.objects.get\
            (pk=self.kwargs.get('fooditem_id', None))
        return reverse('manage_menu',
                       kwargs={'restaurant_id': fooditem.restaurant.id})

