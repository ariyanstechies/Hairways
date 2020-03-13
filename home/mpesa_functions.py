import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
from datetime import datetime
from django.http import HttpResponse, JsonResponse
import base64
import json


class Mpesa:

    def get_access_token(self):
        consumer_key = settings.CONSUMER_KEY
        consumer_secret = settings.CONSUMER_SECRET
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

        response = requests.get(api_URL, auth=HTTPBasicAuth(
            consumer_key, consumer_secret))

        return json.loads(response.text)['access_token']

    def timestamp(self):
        return datetime.now().strftime('%Y%m%d%H%M%S')

    def lipa_na_mpesa_password(self, timestamp):
        pass_key = settings.PASS_KEY
        paying_time = timestamp
        short_code = settings.SHORT_CODE

        data_to_encode = short_code + pass_key + paying_time
        encoded_data = base64.b64encode(data_to_encode.encode())
        encoded_password = encoded_data.decode('utf-8')

        return encoded_password

    def register_url(self, access_token):
        url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
        headers = {"Authorization": "Bearer %s" % access_token}
        body = {
            "ShortCode": '601426',
            "ResponseType": "Completed",
            "ConfirmationURL": "https://1a662ab5.ngrok.io/api/v1/confirmation",
            "ValidationURL": "https://1a662ab5.ngrok.io/api/v1/validation"
        }

        response = requests.post(url=url, json=body, headers=headers)
        return HttpResponse(response)

    def lipa_na_mpesa_online(self, access_token, password, timestamp, phone_no, package_amount, package_name, salon_owner):
        access_token = access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        body = {
            "BusinessShortCode": settings.SHORT_CODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": package_amount,
            "PartyA": phone_no,
            "PartyB": settings.SHORT_CODE,
            "PhoneNumber": phone_no,
            "CallBackURL": "https://6778fbfc.ngrok.io/api/v1/confirmation",
            "AccountReference": salon_owner,
            "TransactionDesc": package_name
        }
        response = requests.post(api_url, json=body, headers=headers)
        return HttpResponse('success')
