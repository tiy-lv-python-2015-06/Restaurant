from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

import restaurant

from restaurant.views import RestaurantProfile, OrderList, RestaurantCreate
from django.contrib.auth import views as auth_views

from restaurant.views import RestaurantProfile, OrderList, CreateMenu, \
    UpdateMenu, ManageMenu, DeleteItem


urlpatterns = [

    url(r'^restaurant_profile/(?P<restaurant_id>[0-9]+)/',
        RestaurantProfile.as_view(), name='restaurant_profile'),

    # url(r'^order_list/', OrderList.as_view(), name='order_list'),

    url(r'^register/restaurant/', RestaurantCreate.as_view(), name='rest_reg'),

    url(r'^order_list/(?P<restaurant_id>[0-9]+)',
        OrderList.as_view(), name='order_list'),

    url(r'^create_menu/(?P<restaurant_id>[0-9]+)',
        CreateMenu.as_view(), name='create_menu'),

    url(r'^update_menu/(?P<fooditem_id>[0-9]+)',
        UpdateMenu.as_view(), name='update_menu'),

    url(r'^delete_menu_item/(?P<fooditem_id>[0-9]+)',
        DeleteItem.as_view(), name='delete_menu_item'),

    url(r'^manage_menu/(?P<restaurant_id>[0-9]+)',
        ManageMenu.as_view(), name='manage_menu'),

]

