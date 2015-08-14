from django.contrib import admin
from customer.models import Customer, Order
from restaurant.models import Restaurant, FoodItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'address', 'city',
                    'state', 'zip', 'phone',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'customer', 'menu', 'timestamp')


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'name', 'price', 'description')
