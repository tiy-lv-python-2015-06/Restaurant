from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
#
from customer.views import CustomerCreate

urlpatterns = [

    url(r'^register/customer/', CustomerCreate.as_view(), name='cust_reg'),
]