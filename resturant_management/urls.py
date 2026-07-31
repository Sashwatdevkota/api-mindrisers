from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    # path("home/", home),
    path("index/", index),
    # path("category/", category_list),
    # path("category/<id>", category_detail),
    # path("table/", table_list),
    # path("table/<id>", table_detail),
    # CLASS BASED
    # path("category/", CategoryView.as_view()),
    # path("category/<id>", CategoryView_Detail.as_view()),
    # GENERIC APIS
    # path("category/", CategoryGeneric.as_view()),
    # path("category/<id>", CategoryGeneric_Detail.as_view()),
    path("table/", TableGeneric.as_view()),
    path("table/<pk>", TableDetailGeneric.as_view()),
]
