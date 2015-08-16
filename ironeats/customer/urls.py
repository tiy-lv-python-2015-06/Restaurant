from django.conf.urls import url
#
import customer
from customer.views import PlaceOrder, Confirm

urlpatterns = [
        url(r'^(?P<pk>[0-9]+)/', customer.views.menu, name='menu'),
        url(r'^order/(?P<pk>[0-9]+)/', PlaceOrder.as_view(), name='order'),
            url(r'^confirm/(?P<pk>[0-9]+)/', Confirm.as_view(), name='confirm'),
]