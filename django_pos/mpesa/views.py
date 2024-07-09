from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from .credentials import MpesaAccessToken, LipanaMpesaPpassword

from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'mpesa/home.html', {'navbar': 'home'})


def token(request):
    consumer_key = 'NZQ9NUVfB35mBhsPPMK7u0Me1TVqSHqNuqECEqPjGiUFObaY'
    consumer_secret = 'HiqF3viiZmhGAsF3GYfU4PNuH9fNgXdWM1HFNAQiYA0dPaIat1m4qqDvBdhBGOE5'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'mpesa/token.html', {"token": validated_mpesa_access_token})


def pay(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Clean Farm Agrovet",
            "TransactionDesc": "goods cost",
        }

    response = requests.post(api_url, json=request, headers=headers)

    return redirect('mpesa:success')


def stk(request):
    return render(request, 'mpesa/pay.html', {'navbar': 'stk'})

def success(request):
    return render(request, 'mpesa/success.html')