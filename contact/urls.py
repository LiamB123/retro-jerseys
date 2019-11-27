from django.conf.urls import url
from .views import contact_form, sales_form

urlpatterns=[
    url(r'^chat-us', contact_form, name="contact"),

    ]