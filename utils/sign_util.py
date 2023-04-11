import hashlib


def sign_with_sha256(secret_key, data):
   """使用 SHA256 算法对数据进行签名

   参数:
       secret_key (str): 密钥字符串
       data (str): 待签名字符串

   返回:
       str: 签名后的字符串
   """
   secret_key = secret_key.encode('utf-8')
   data = data.encode('utf-8')
   signature = hmac.new(secret_key, msg=data, digestmod=hashlib.sha256).hexdigest()
   return signature
