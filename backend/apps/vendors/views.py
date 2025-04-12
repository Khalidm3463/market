from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VendorRegistrationSerializer

class VendorRegistrationView(APIView):
    def post(self, request):
        serializer = VendorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            vendor = serializer.save()
            return Response(
                {"shop_name": vendor.shop_name, "email": vendor.user.email},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)