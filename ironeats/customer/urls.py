from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
#
urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),
    # url(r'/login/', auth_views.login,
    #     {'restaurant_login.html': 'templates/registration/restaurant_login.html'}, name='login'),
]