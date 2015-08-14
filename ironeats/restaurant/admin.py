from django.contrib import admin
from customer.models import Customer, Order
from restaurant.models import Restaurant, FoodItem


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'address', 'city',
                    'state', 'zip', 'phone',)

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'name', 'price', 'description')
