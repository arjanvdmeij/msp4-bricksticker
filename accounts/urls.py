from django.conf.urls import url, include
from . import urls_reset
from .views import register, profile, staff, logout, login, forgetme, get_mail_csv, toggle_processed

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^staff/$', staff, name='staff'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^forgetme/$', forgetme, name='forgetme'),
    url(r'^dl_csv/$', get_mail_csv, name='dl_csv'),
    url(r'^toggle/(?P<id>\d+)$', toggle_processed, name='toggle'),
    url(r'^password-reset/', include(urls_reset)),
]
