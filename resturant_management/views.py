from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.


@api_view(["GET"])
def category_list(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def table_list(request):
    table = Table.objects.all()
    serializer = TableSerializer(table, many=True)
    return Response(serializer.data)


def index(request):
    return render(request, "index.html")
