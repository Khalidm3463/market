from rest_framework import serializers
from .models import Vendor
from backend.apps.users.models import User

class VendorRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    shop_name = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Vendor
        fields = ["email", "password", "shop_name", "address", "city", "description"]

    def create(self, validated_data):
        # Create User first
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            user_type="VENDOR",
        )
        # Create Vendor linked to the user
        vendor = Vendor.objects.create(
            user=user,
            shop_name=validated_data["shop_name"],
            address=validated_data["address"],
            city=validated_data.get("city", "Dubai"),
            description=validated_data.get("description", ""),
        )
        return vendor