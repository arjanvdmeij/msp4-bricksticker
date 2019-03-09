from django.conf.urls import url, include
from . import urls_reset, urls_staff
from .views import register, profile, logout, login, forgetme

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^forgetme/$', forgetme, name='forgetme'),
    url(r'^password-reset/', include(urls_reset)),
]
