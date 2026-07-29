from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .models import *  # importing all models
from .serializer import *  # importing all serializers(converting queryset to json)

# Create your views here.


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
        return Response({"message": "Data added", "result": serializer.data})


@api_view(["GET"])
def table_list(request):
    table = Table.objects.all()
    serializer = TableSerializer(table, many=True)
    return Response(serializer.data)


def index(request):
    return render(request, "index.html")
