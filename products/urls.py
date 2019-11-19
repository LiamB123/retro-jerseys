from django.conf.urls import url, include
from products.views import all_products

urlpatterns = [
    url(r'^$', all_products, name ='products'),
    ]