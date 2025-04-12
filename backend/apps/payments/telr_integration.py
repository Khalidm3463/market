import requests
import json
from django.conf import settings
from django.urls import reverse

TELR_BASE_URL = "https://secure.telr.com/gateway/order.json"

def create_telr_payment(order, request):
    return_url = request.build_absolute_uri(
        reverse("payment-callback")
    )
    telr_data = {
        "ivp_method": "create",
        "ivp_store": settings.TELR_STORE_ID,
        "ivp_authkey": settings.TELR_AUTH_KEY,
        "ivp_cart": str(order.id),
        "ivp_test": "1" if settings.DEBUG else "0",
        "ivp_amount": str(order.total_price),
        "ivp_currency": "AED",
        "ivp_desc": f"Order #{order.id} - Clothing Delivery App",
        "return_auth": return_url,
        "return_can": return_url,
        "return_decl": return_url,
    }
    response = requests.post(TELR_BASE_URL, data=telr_data)
    return response.json()