from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, MiddleEasternCategoryViewSet

router = DefaultRouter()
router.register(r"categories", MiddleEasternCategoryViewSet, basename="category")
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]