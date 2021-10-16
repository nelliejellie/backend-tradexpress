from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# https://stackoverflow.com/questions/53123092/how-to-send-post-request-to-django-api-from-reactjs-web-app
