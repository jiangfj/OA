from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('tongxun', views.address_book_list),
]
