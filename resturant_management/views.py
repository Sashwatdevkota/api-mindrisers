from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .models import *  # importing all models
from .serializer import *  # importing all serializers(converting queryset to json)

# Create your views here.

# Generic API
from rest_framework.generics import GenericAPIView

# class CategoryGeneric(GenericAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     def get(self, request):  # request handler

#         category = self.get_queryset()
#         serializer = self.serializer_class(category, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"message": "Data added", "result": serializer.data})

# class CategoryGeneric_Detail(GenericAPIView):
# queryset = Category.objects.all()
# serializer_class = CategorySerializer
# lookup_field = "id"

# def get(self, request, id):

#     category = self.get_object()
#     serializers = self.serializer_class(category)
#     return Response(serializers.data)

# def put(self, request, id):

#     category = self.get_object()
#     serializer = CategorySerializer(category, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()

#     return Response(
#         {
#             "message": "Data updated successfully",
#             "result": serializer.data,
#         }
#     )

# def delete(self, request, id):

#     category = self.get_object()
#     item = OrderMenu.objects.filter(menu__category=category).count()
#     if item > 0:
#         return Response(
#             {
#                 "message": "Data can not be deleted. Protected Foreign Key in Order Menu"
#             }
#         )
#     category.delete()
#     return Response({"message": "Data has been deleted"})


class TableGeneric(GenericAPIView):

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


class TableDetailGeneric(GenericAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get(self, request, pk):

        table = self.get_object()
        serializers = self.serializer_class(table)
        return Response(serializers.data)

    def put(self, request, pk):

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

    def delete(self, request, pk):
        table = self.get_object()
        table.delete()
        return Response({"message": "Data has been deleted"})


#############################
# CLASS BASED API
##############################

# from rest_framework.views import APIView

# class CategoryView(APIView):
#     def get(self, request):  # request handler

#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)

#     def post(self, request):

#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"message": "Data added", "result": serializer.data})

# class CategoryView_Detail(APIView):

#     def get(self, request, id):

#         category = Category.objects.get(id=id)
#         serializers = CategorySerializer(category)
#         return Response(serializers.data)

#     def put(self, request, id):

#         category = Category.objects.get(id=id)
#         serializer = CategorySerializer(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(
#             {
#                 "message": "Data updated successfully",
#                 "result": serializer.data,
#             }
#         )

#     def delete(self, request, id):

#         category = Category.objects.get(id=id)
#         item = OrderMenu.objects.filter(menu__category=category).count()
#         if item > 0:
#             return Response(
#                 {
#                     "message": "Data can not be deleted. Protected Foreign Key in Order Menu"
#                 }
#             )
#         category.delete()
#         return Response({"message": "Data has been deleted"})

###########################
# FUNCTION BASED API
###############################

# @api_view(["GET", "POST"])
# def category_list(request):
#     if request.method == "GET":
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"message": "Data added", "result": serializer.data})


# @api_view(["GET", "DELETE", "PUT"])
# def category_detail(request, id):
#     category = Category.objects.get(id=id)
#     if request.method == "GET":
#         serializers = CategorySerializer(category)
#         return Response(serializers.data)

#     elif request.method == "PUT":
#         serializer = CategorySerializer(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(
#             {
#                 "message": "Data updated successfully",
#                 "result": serializer.data,
#             }
#         )

#     elif request.method == "DELETE":
#         item = OrderMenu.objects.filter(menu__category=category).count()
#         if item > 0:
#             return Response(
#                 {
#                     "message": "Data can not be deleted. Protected Foreign Key in Order Menu"
#                 }
#             )
#         category.delete()
#         return Response({"message": "Data has been deleted"})


# @api_view(["GET", "POST"])
# def table_list(request):
#     if request.method == "GET":
#         table = Table.objects.all()
#         serializer = TableSerializer(table, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = TableSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"message": "Data added", "result": serializer.data})


# @api_view(["GET", "DELETE", "PUT"])
# def table_detail(request, id):
#     table = Table.objects.get(id=id)
#     if request.method == "GET":
#         serializers = TableSerializer(table)
#         return Response(serializers.data)

#     elif request.method == "PUT":
#         serializer = TableSerializer(table, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(
#             {
#                 "message": "Data updated successfully",
#                 "result": serializer.data,
#             }
#         )

#     elif request.method == "DELETE":

#         table.delete()
#         return Response({"message": "Data has been deleted"})


def index(request):
    return render(request, "index.html")
