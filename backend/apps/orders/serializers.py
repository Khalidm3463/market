from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["product", "quantity", "price"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "user", "items", "total_price", "delivery_address", "status"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        total = 0
        for item_data in items_data:
            product = item_data["product"]
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item_data["quantity"],
                price=product.price * item_data["quantity"],
            )
            total += product.price * item_data["quantity"]
        order.total_price = total
        order.save()
        return order