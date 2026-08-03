from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("index/", index),
    #
    path("category/", CategoryConcreteGeneric.as_view()),
    path("category/<id>/", CategoryDetailConcreteGeneric.as_view()),
    #
    path("table/", TableConcreteGeneric.as_view()),
    path("table/<id>/", TableDetailConcreteGeneric.as_view()),
]
