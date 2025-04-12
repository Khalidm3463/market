from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from .models import Product, MiddleEasternCategory
from .serializers import ProductSerializer, MiddleEasternCategorySerializer

class MiddleEasternCategoryViewSet(viewsets.ModelViewSet):
    queryset = MiddleEasternCategory.objects.all()
    serializer_class = MiddleEasternCategorySerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can edit categories

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Filter by Middle Eastern category (e.g., ?category=kaftans)
        category_slug = self.request.query_params.get("category")
        if category_slug:
            return Product.objects.filter(category__slug=category_slug, is_active=True)
        return Product.objects.filter(is_active=True)

    def perform_create(self, serializer):
        # Auto-set vendor to the logged-in user's vendor profile
        if self.request.user.user_type == "VENDOR":
            serializer.save(vendor=self.request.user.vendor_profile)
        else:
            # raise PermissionDenied("Only vendors can create products")
            raise PermissionError("Only vendors can create products")