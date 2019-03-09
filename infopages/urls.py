from django.conf.urls import url, include
from .views import about, privacy, terms_and_conditions, returns, add_faq

urlpatterns = [
    url(r'^about/$', about, name='about'),
    url(r'^privacy/$', privacy, name='privacy'),
    url(r'^terms/$', terms_and_conditions, name='terms_and_conditions'),
    url(r'^returns/$', returns, name='returns'),
    ]