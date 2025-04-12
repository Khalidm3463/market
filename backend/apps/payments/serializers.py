from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["method", "amount", "status"]

class TelrPaymentSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    method = serializers.ChoiceField(choices=Payment.PAYMENT_METHODS)