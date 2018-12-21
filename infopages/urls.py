from django.conf.urls import url, include
# from products.views import all_products
from .views import about, privacy, terms_and_conditions, returns

urlpatterns = [
    url(r'^about/$', about, name='about'),
    url(r'^privacy/$', privacy, name='privacy'),
    url(r'^terms/$', terms_and_conditions, name='terms_and_conditions'),
    url(r'^returns/$', returns, name='returns'),
    ]