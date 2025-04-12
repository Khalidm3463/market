from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ("CUSTOMER", "Customer"),
        ("VENDOR", "Vendor"),
        ("DRIVER", "Driver")
    )

    email = models.EmailField(unique = True)
    user_type = models.CharField(max_length = 10, choices = USER_TYPE_CHOICES, default = "CUSTOMER")
    phone = models.CharField(max_length=15, blank=True)
    preferred_language = models.CharField(max_length=2, default="en")


    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email