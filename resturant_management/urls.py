from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    # path("home/", home),
    path("index/", index),
    path("category/", category_list),
    path("category/<id>", category_detail),
    path("table/", table_list),
    path("table/<id>", table_detail),
]
