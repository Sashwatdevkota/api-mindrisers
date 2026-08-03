from django.shortcuts import render

from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet


from .models import Category, Table, OrderMenu
from .serializer import (
    CategorySerializer,
    TableSerializer,
)  # importing serializers(converting queryset to json)

###############################################
# View Set
###############################################


class CategoryViewSet(ViewSet):
    def list(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Data added", "result": serializer.data})


class CategoryDetailViewSet(ViewSet):
    def retrieve(self, request, id):
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def update(self, request, id):
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

    def destroy(self, request, id):
        category = Category.objects.get(id=id)

        item = OrderMenu.objects.filter(menu__category=category).count()

        if item > 0:
            return Response(
                {"message": "Data can't be deleted. Protected Foreign Key in OrderMenu"}
            )

        category.delete()
        return Response({"message": "Data has been deleted."})


###############################################
# Concrete Generic Views
###############################################


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


###############################################
# Function Based Views (FBV)
###############################################


@api_view(["GET", "POST"])
def category_list(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Data added",
                "result": serializer.data,
            }
        )


@api_view(["GET", "PUT", "DELETE"])
def category_detail(request, id):
    category = Category.objects.get(id=id)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Data updated successfully",
                "result": serializer.data,
            }
        )

    elif request.method == "DELETE":
        item = OrderMenu.objects.filter(menu__category=category).count()

        if item > 0:
            return Response(
                {"message": "Data can't be deleted. Protected Foreign Key in OrderMenu"}
            )

        category.delete()
        return Response({"message": "Data has been deleted."})


@api_view(["GET", "POST"])
def table_list(request):
    if request.method == "GET":
        table = Table.objects.all()
        serializer = TableSerializer(table, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TableSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Data added",
                "result": serializer.data,
            }
        )


@api_view(["GET", "PUT", "DELETE"])
def table_detail(request, id):
    table = Table.objects.get(id=id)

    if request.method == "GET":
        serializer = TableSerializer(table)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TableSerializer(table, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Data updated successfully",
                "result": serializer.data,
            }
        )

    elif request.method == "DELETE":
        table.delete()
        return Response({"message": "Data has been deleted."})


def index(request):
    return render(request, "index.html")
