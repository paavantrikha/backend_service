from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('user_id', 'email', 'username', 'is_active')