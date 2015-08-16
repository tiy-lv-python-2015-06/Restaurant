from django.contrib import admin
from restaurant.models import Restaurant, FoodItem


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('user', 'business_name', 'address', 'city',
                    'state', 'zip_code', 'phone_number',)


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'name', 'price', 'description')
