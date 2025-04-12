from django.db import models
from backend.apps.orders.models import Order

class Payment(models.Model):
    PAYMENT_METHODS = (
        ("TELR", "Telr"),
        ("COD", "Cash on Delivery"),
    )
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    )

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default="COD")
    transaction_id = models.CharField(max_length=255, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"