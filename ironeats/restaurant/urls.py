from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from restaurant.views import RestaurantProfile

urlpatterns = [

    url(r'^restaurant_profile/', RestaurantProfile.as_view(),
        name='restaurant_profile'),

]