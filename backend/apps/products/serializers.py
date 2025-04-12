from rest_framework import serializers
from .models import Product, MiddleEasternCategory

class MiddleEasternCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MiddleEasternCategory
        fields = ["id", "name", "slug", "description"]

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", queryset=MiddleEasternCategory.objects.all())
    vendor = serializers.StringRelatedField()  # Show vendor's shop name

    class Meta:
        model = Product
        fields = [
            "id", "name", "category", "vendor",
            "price", "size_guide", "fabric_type", "occasion", "stock"
        ]