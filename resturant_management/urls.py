from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    # path("home/", home),
    path("index/", index),
    path("category/", category_list),
    path("table/", table_list),
]
