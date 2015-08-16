from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView, CreateView
from customer.models import Order
from restaurant.models import Restaurant, FoodItem


class Home(ListView):
    model = Restaurant
    template_name = "home.html"
    queryset = Restaurant.objects.all()
    context_object_name = 'restaurant'
    paginate_by = 20

def menu(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    FoodInlineFormSet = inlineformset_factory(Restaurant, FoodItem,
                                              fields=('qty',), extra=0, )
    if request.method == "POST":
        formset = FoodInlineFormSet(request.POST, request.FILES, instance=Restaurant)
        formset.save()
        return HttpResponse('print something at least')
    else:
        formset = FoodInlineFormSet(instance=restaurant)

    return render(request, "order/menu.html", context={
        'formset': formset, 'zipped': zip(formset,restaurant.fooditem_set.all()), 'pk': pk })
