from django.conf.urls import url
from .views import all_products, product_detail, add_product

urlpatterns = [
    url(r'^$',all_products,name='products'),
    url(r'^(?P<pk>\d+)/$',product_detail,name='productdetail'),
    ]