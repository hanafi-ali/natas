import base64
import json
from urllib import parse

from config import password_length, natas11_default_color
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 11


def xor_encrypt(text: str, key: str) -> str:
    encrypted = ""

    for i in range(len(text)):
        encrypted += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    return encrypted


def find_key_and_encrypt_data(code: str, data: str) -> str:
    enc = xor_encrypt(code, data)
    key = enc[:enc.find(enc[0], 1)]
    data = json.dumps({"showpassword": "yes", "bgcolor": natas11_default_color}).replace(" ", "")
    return str(base64.b64encode(xor_encrypt(data, key).encode("utf-8")), "utf-8")


def get_secret():
    req = get_request_object(level_number)
    url = get_level_url(level_number)
    result = req.get(url)

    if result.status_code == 200:
        code = result.cookies.get("data")
        code = str(base64.b64decode(parse.unquote(code)), "utf-8")
        data = json.dumps({"showpassword": "no", "bgcolor": natas11_default_color}).replace(" ", "")

        encrypted_data = find_key_and_encrypt_data(code, data)

        req = get_request_object(level_number)
        result = req.get(url, cookies={"data": encrypted_data})
        text = result.text
        search = "The password for natas12 is"

        if search in text:
            start_index = text.find(search) + len(search) + 1
            return text[start_index: start_index + password_length]

    return ""


secret = get_secret()
store_secret_and_print_message(level_number, secret)
