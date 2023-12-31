from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for User model (CRUD).

    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
