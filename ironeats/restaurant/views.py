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


class OrderList(DetailView):
    model = Restaurant
    pk_url_kwarg = 'restaurant_id'
    template_name = 'restaurant/order_list.html'

    # model = Order
    # template_name = "restaurant/order_list.html"
    # queryset = Order.objects.all().order_by('timestamp')
    # paginate_by = 20


class CreateMenu(CreateView):
    model = FoodItem
    fields = ('name', 'price', 'description', 'category', )
    success_url = reverse_lazy('update_menu')
    template_name = "restaurant/create_menu.html"

    def get_success_url(self):
        return reverse('update_menu',
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


class UpdateMenu(UpdateView):
    model = FoodItem
    fields = ['name', 'price', 'description', 'category', ]
    pk_url_kwarg = 'restaurant_id'
    template_name = "restaurant/update_menu.html"

    def get_context_data(self, **kwargs):
        context = super(UpdateMenu, self).get_context_data(**kwargs)
        # context['restaurant_id'] = self.kwargs.get('restaurant_id', None)
        context['restaurant'] = Restaurant.objects.get(
            pk=self.kwargs.get('restaurant_id', None))
        return context

    # def get_queryset(self):
    #     rest_id = self.kwargs.get('restaurant_id', None)
    #     queryset = Restaurant.objects.get(pk=rest_id).get_menu_items()
    #     return queryset

    def get_success_url(self):
        return reverse('update_menu')


# def RestMenu(request, pk):
#     restaurant = Restaurant.objects.get(pk=pk)
#     FoodInlineFormSet = inlineformset_factory(Restaurant, FoodItem, fields=('qty',))
#     if request.method == "POST":
#         formset = FoodInlineFormSet(request.POST, request.FILES, instance=restaurant)
#         if formset.is_valid():
#             formset.save()
#             # Do something. Should generally end with a redirect. For example:
#             return HttpResponse('')
#     else:
#         formset = FoodInlineFormSet(instance=restaurant)
#     return render_to_response("order/menu.html", {
#         "formset": formset,
#     })


class DeleteMenu(DeleteView):
    model = FoodItem