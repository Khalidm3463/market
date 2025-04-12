from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "user_type", "phone", "preferred_language"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            user_type=validated_data.get("user_type", "CUSTOMER"),
            phone=validated_data.get("phone", ""),
            preferred_language=validated_data.get("preferred_language", "en"),
        )
        return user

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_type"] = user.user_type
        return token

class UserLoginSerializer(CustomTokenObtainSerializer):
    pass