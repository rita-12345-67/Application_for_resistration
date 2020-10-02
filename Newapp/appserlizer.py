from rest_framework.serializers import ModelSerializer
from Newapp.models import Userinfo

class Userserlizer(ModelSerializer):
    class Meta:
        model = Userinfo
        fields= '__all__'
