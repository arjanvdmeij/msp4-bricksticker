from django.conf.urls import url
from products.views import add_product
from .views import get_mail_csv
from checkout.views import order_handling, toggle_processed
from infopages.views import add_faq

urlpatterns = [
    url(r'^$', order_handling, name='staff'),
    url(r'^orders/$', order_handling, name='orders'),
    url(r'^add_product/$', add_product, name='add_product'),
    url(r'^add_faq/$', add_faq, name='add_faq'),
    url(r'^dl_csv/$', get_mail_csv, name='dl_csv'),
    url(r'^toggle/(?P<id>\d+)$', toggle_processed, name='toggle'),
]
