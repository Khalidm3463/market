from django.db import models
from backend.apps.users.models import User
from backend.apps.products.models import Product

class Order(models.Model):
    ORDER_STATUS = (
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("SHIPPED", "Shipped"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField(null=True)  # For 1-hour delivery promise

    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"
