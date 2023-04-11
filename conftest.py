import pytest
import requests

from utils.encrypt_util import EncryptUtil
from utils.sign_util import SignUtil


@pytest.fixture(scope="session")
def base_url():
    """
    定义测试基础 URL
    """
    return "https://dec-api-testnet.pundix.com"


@pytest.fixture(scope="session")
def session():
    """
    定义测试 session
    """
    return requests.Session()


@pytest.fixture(scope="session")
def encrypt_util():
    """
    定义加解密工具类实例
    """
    return EncryptUtil()


@pytest.fixture(scope="session")
def sign_util():
    """
    定义签名工具类实例
    """
    return SignUtil()
