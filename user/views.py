from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username == "" or password == "":
            return Response(
                {"error": "Username and password are required."}, status=400
            )
        user = authenticate(request, username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "username": username})
        else:
            return Response({"error": "Invalid credentials."}, status=401)
