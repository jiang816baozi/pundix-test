import hashlib
import hmac
import base64

class EncryptUtil:
    def encrypt_with_hmac_sha256(key, data):
        """使用 HMAC-SHA256 算法对数据进行加密

        参数:
            key (str): 密钥字符串
            data (str): 待加密字符串

        返回:
            str: 加密后的字符串
        """
        key = key.encode('utf-8')
        data = data.encode('utf-8')
        signature = hmac.new(key, msg=data, digestmod=hashlib.sha256).digest()
        return base64.b64encode(signature).decode('utf-8')
