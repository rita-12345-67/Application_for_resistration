from rest_framework.serializers import ModelSerializer
from Newapp.models import Userinfo

class UserSerializer(ModelSerializer):
    class Meta:
        model = Userinfo
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Userinfo
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Userinfo.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        # "token": AuthToken.objects.create(user)[1]
        return user

from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
    model = Userinfo

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)