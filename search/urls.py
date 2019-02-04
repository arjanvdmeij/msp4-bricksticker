from django.conf.urls import url
from .views import search, filter_products

urlpatterns = [
    url(r'^$', filter_products, name='filter_products'),
    url(r'^search/$', search, name='search'),
    ]