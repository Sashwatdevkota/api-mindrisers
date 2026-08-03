from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .models import *  # importing all models
from .serializer import *  # importing all serializers(converting queryset to json)

###############################################
# Concrete Generic Views
###############################################

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


class CategoryConcreteGeneric(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailConcreteGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"

    def delete(self, request, id):
        category = self.get_object()

        item = OrderMenu.objects.filter(menu__category=category).count()

        if item > 0:
            return Response(
                {"message": "Data can't be deleted. Protected Foreign Key in OrderMenu"}
            )

        category.delete()
        return Response({"message": "Data has been deleted."})


class TableConcreteGeneric(ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDetailConcreteGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_field = "id"

    def delete(self, request, id):
        table = self.get_object()
        table.delete()
        return Response({"message": "Data has been deleted."})


###############################################
# GenericAPIView + Mixins
###############################################

from rest_framework.generics import GenericAPIView
from rest_framework import mixins


class CategoryMixinGeneric(
    GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetailMixinGeneric(
    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"

    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request)

    def delete(self, request, id):
        category = self.get_object()

        item = OrderMenu.objects.filter(menu__category=category).count()

        if item > 0:
            return Response(
                {"message": "Data can't be deleted. Protected Foreign Key in OrderMenu"}
            )

        category.delete()
        return Response({"message": "Data has been deleted."})


class TableMixinGeneric(
    GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class TableDetailMixinGeneric(
    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_field = "id"

    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request)

    def delete(self, request, id):
        table = self.get_object()
        table.delete()
        return Response({"message": "Data has been deleted."})
