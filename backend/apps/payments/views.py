from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from backend.apps.orders.models import Order
from .models import Payment
from .telr_integration import create_telr_payment
from .serializers import PaymentSerializer, TelrPaymentSerializer

class InitiatePaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TelrPaymentSerializer(data=request.data)
        if serializer.is_valid():
            order = Order.objects.get(id=serializer.data["order_id"], user=request.user)
            
            # Create Payment record
            payment = Payment.objects.create(
                order=order,
                method=serializer.data["method"],
                amount=order.total_price
            )

            if serializer.data["method"] == "TELR":
                telr_response = create_telr_payment(order, request)
                if telr_response.get("order"):
                    payment.transaction_id = telr_response["order"]["ref"]
                    payment.save()
                    return Response({"payment_url": telr_response["order"]["url"]})
                return Response({"error": "Telr payment failed"}, status=400)
            
            # Handle Cash on Delivery
            payment.status = "COMPLETED"
            payment.save()
            return Response({"status": "COD payment confirmed"})
        return Response(serializer.errors, status=400)

class PaymentCallbackView(APIView):
    def post(self, request):
        transaction_id = request.data.get("order")["ref"]
        payment = Payment.objects.get(transaction_id=transaction_id)
        
        if request.data.get("order")["status"] == "3":
            payment.status = "COMPLETED"
        else:
            payment.status = "FAILED"
        
        payment.save()
        return Response({"status": "callback processed"})