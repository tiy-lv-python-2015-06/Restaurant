from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from restaurant.views import RestaurantProfile, OrderList, CreateMenu, \
    UpdateMenu

urlpatterns = [

    url(r'^restaurant_profile/(?P<restaurant_id>[0-9]+)/',
        RestaurantProfile.as_view(), name='restaurant_profile'),

    url(r'^order_list/(?P<restaurant_id>[0-9]+)',
        OrderList.as_view(), name='order_list'),

    url(r'^create_menu/(?P<restaurant_id>[0-9]+)',
        CreateMenu.as_view(), name='create_menu'),

    url(r'^update_menu/(?P<restaurant_id>[0-9]+)',
        UpdateMenu.as_view(), name='update_menu'),
]