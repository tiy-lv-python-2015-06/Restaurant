from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from restaurant.views import RestaurantProfile, OrderList
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^restaurant_profile/(?P<restaurant_id>[0-9]+)/',
        RestaurantProfile.as_view(), name='restaurant_profile'),
    url(r'^order_list/', OrderList.as_view(), name='order_list'),
        url(r'^', include('django.contrib.auth.urls')),
    url(r'/login/', auth_views.login,
        {'login.html': 'templates/registration/login.html'}, name='login'),

]
