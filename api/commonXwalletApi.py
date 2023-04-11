# api/commonXwalletApi.py

import requests
import json

class CommonXwalletApi:
    def __init__(self, url):
        self.url = url

    def generate_aes_key(self, nonce, secret, sign, timestamp):
        headers = {"Content-Type": "application/json"}
        data = {
            "nonce": nonce,
            "secret": secret,
            "sign": sign,
            "timestamp": timestamp
        }
        response = requests.post(self.url + "/api/v1/encrypt/generate", data=json.dumps(data), headers=headers)
        return response.json()
