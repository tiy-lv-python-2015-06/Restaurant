from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
import restaurant

from restaurant.views import RestaurantProfile, OrderList, RestaurantCreate
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^restaurant_profile/(?P<restaurant_id>[0-9]+)/',
        RestaurantProfile.as_view(), name='restaurant_profile'),
    url(r'^order_list/', OrderList.as_view(), name='order_list'),
    url(r'^register/business/', RestaurantCreate.as_view(), name='rest_reg'),
    url(r'^register/', restaurant.views.createuser, name='create_user')

]
