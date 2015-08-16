from django.conf.urls import url
#

urlpatterns = [
        url(r'^(?P<pk>[0-9]+)/', 'customer.views.menu', name='menu'),
]