from django.conf.urls import include, url
from django.contrib import admin
import customer
from customer.views import Home
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^', include('django.contrib.auth.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', Home.as_view(), name='home'),

    url(r'^restaurant/', include('restaurant.urls')),

    url(r'^customer/', include('customer.urls')),

    url(r'restaurant/login/', auth_views.login,
        {'extra_context': {'next': '/'}}, name='rest_login'),

    url(r'customer/login/', auth_views.login,
        {'extra_context': {'next': '/'}}, name='cust_login'),

    url(r'^register/', customer.views.createuser, name='create_user'),

]
