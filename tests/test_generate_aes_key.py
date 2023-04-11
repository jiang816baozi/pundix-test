# tests/test_generate_aes_key.py

import pytest
from api.commonXwalletApi import CommonXwalletApi
from config import config
from utils import encrypt_util, sign_util

def test_generate_aes_key():
    common_api = CommonXwalletApi(config['common']['url'])

    nonce = "test_nonce"
    secret = "test_secret"
    timestamp = 1234567890
    sign = sign_util.generate_sign(nonce, secret, timestamp)
    response = common_api.generate_aes_key(nonce, secret, sign, timestamp)

    assert response['code'] == 0
    assert response['data']['aesKey']
    assert encrypt_util.decrypt(response['data']['aesKey'], secret) == "This is a test message."
