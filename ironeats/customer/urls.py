from django.conf.urls import url
#
from customer.views import CustomerCreate, Confirm

import customer
from customer.views import PlaceOrder

urlpatterns = [

    url(r'^register/customer/', 'customer.views.createuser', name='cust_reg'),

    url(r'^(?P<pk>[0-9]+)/', customer.views.menu, name='menu'),

    url(r'^order/(?P<pk>[0-9]+)/', PlaceOrder.as_view(), name='order'),

    url(r'^confirm/', Confirm.as_view(), name='confirm'),

]
