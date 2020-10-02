from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Newapp.appserlizer import Userserlizer
from Newapp.models import Userinfo
class Userview(ModelViewSet):
    """ create viewset for User"""
    queryset = Userinfo.objects.all()
    serializer_class = Userserlizer
