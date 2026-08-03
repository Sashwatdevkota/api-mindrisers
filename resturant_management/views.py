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


###############################################
# GenericAPIView
###############################################

# from rest_framework.generics import GenericAPIView


class CategoryGenericAPIView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        category = self.get_queryset()
        serializer = self.serializer_class(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Data added", "result": serializer.data})


class CategoryDetailGenericAPIView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"

    def get(self, request, id):
        category = self.get_object()
        serializer = self.serializer_class(category)
        return Response(serializer.data)

    def put(self, request, id):
        category = self.get_object()
        serializer = self.serializer_class(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Data updated successfully",
                "result": serializer.data,
            }
        )

    def delete(self, request, id):
        category = self.get_object()

        item = OrderMenu.objects.filter(menu__category=category).count()

        if item > 0:
            return Response(
                {"message": "Data can't be deleted. Protected Foreign Key in OrderMenu"}
            )

        category.delete()
        return Response({"message": "Data has been deleted."})


class TableGenericAPIView(GenericAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get(self, request):
        table = self.get_queryset()
        serializer = self.serializer_class(table, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Data added", "result": serializer.data})


class TableDetailGenericAPIView(GenericAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_field = "id"

    def get(self, request, id):
        table = self.get_object()
        serializer = self.serializer_class(table)
        return Response(serializer.data)

    def put(self, request, id):
        table = self.get_object()
        serializer = self.serializer_class(table, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Data updated successfully",
                "result": serializer.data,
            }
        )

    def delete(self, request, id):
        table = self.get_object()
        table.delete()
        return Response({"message": "Data has been deleted."})


###############################################
# APIView
###############################################

from rest_framework.views import APIView


class CategoryAPIView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "Data added",
                "result": serializer.data,
            }
        )


class CategoryDetailAPIView(APIView):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, id):
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Data updated successfully",
                "result": serializer.data,
            }
        )

    def delete(self, request, id):
        category = Category.objects.get(id=id)

        item = OrderMenu.objects.filter(menu__category=category).count()

        if item > 0:
            return Response(
                {"message": "Data can't be deleted. Protected Foreign Key in OrderMenu"}
            )

        category.delete()
        return Response({"message": "Data has been deleted."})


class TableAPIView(APIView):
    def get(self, request):
        table = Table.objects.all()
        serializer = TableSerializer(table, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TableSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "Data added",
                "result": serializer.data,
            }
        )


class TableDetailAPIView(APIView):
    def get(self, request, id):
        table = Table.objects.get(id=id)
        serializer = TableSerializer(table)
        return Response(serializer.data)

    def put(self, request, id):
        table = Table.objects.get(id=id)
        serializer = TableSerializer(table, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Data updated successfully",
                "result": serializer.data,
            }
        )

    def delete(self, request, id):
        table = Table.objects.get(id=id)
        table.delete()
        return Response({"message": "Data has been deleted."})
