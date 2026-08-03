from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("index/", index),
    #
    path(
        "category/",
        CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "category/<int:id>/",
        CategoryDetailViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
            }
        ),
    ),
    #
    path("table/", TableConcreteGeneric.as_view()),
    path("table/<id>/", TableDetailConcreteGeneric.as_view()),
    #
]
