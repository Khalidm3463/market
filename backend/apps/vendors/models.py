from django.db import models
from backend.apps.users.models import User
# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendor_profile")
    shop_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, default="Dubai")
    logo = models.ImageField(upload_to="vendor_logos/", blank=True)
    is_approved = models.BooleanField(default=False)  # Admin must approve vendors
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shop_name
    
    