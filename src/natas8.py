import base64
import binascii
import html
import re

from config import password_length, natas8_code_length
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 8


def get_secret():
    req = get_request_object(level_number)
    url = get_level_url(level_number)
    result = req.get(url + "/index-source.html")
    pattern = "<[^<]+?>"
    text = re.sub(pattern, "", html.unescape(result.text))
    search = "$encodedSecret"

    if search in text:
        start_index = text.find(search) + len(search) + 4
        code = text[start_index: start_index + natas8_code_length]
        code = str(base64.b64decode(str(binascii.unhexlify(code), "utf-8")[::-1]), "utf-8")
        result = req.post(url, data={"secret": code, "submit": "1"})
        text = result.text
        search = "The password for natas9 is"

        if search in text:
            start_index = text.find(search) + len(search) + 1
            return text[start_index: start_index + password_length]

    return ""


secret = get_secret()
store_secret_and_print_message(level_number, secret)
