from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        nombre_usuario = request.data.get('user', None)
        password = request.data.get('password', None)
        user = authenticate(username=nombre_usuario, password=password)
        if user:
            login(request, user)
            return Response(
                status=status.HTTP_200_OK)
        return Response(
            status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class Login(TemplateView):
    template_name = 'login/index.html'
