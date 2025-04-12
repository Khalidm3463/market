from django.db import models
from backend.apps.vendors.models import Vendor
# Create your models here.

class MiddleEasternCategory(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Kaftans", "Abayas"
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name
    

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(MiddleEasternCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size_guide = models.JSONField(default=dict)  # e.g., {"US": "M", "EU": "42"}
    fabric_type = models.CharField(max_length=100)
    occasion = models.CharField(max_length=100, blank=True)  # e.g., "Eid", "Wedding"
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name