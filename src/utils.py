# this file contains util functions used in the project

import requests

from config import base_url, password_length, secrets_folder


def get_level_url(level_number: int) -> str:
    return f"http://natas{level_number}.{base_url}"


def get_password(level_number: int) -> str:
    with open(f"{secrets_folder}/natas{level_number}.txt", "r") as file:
        return file.read()


def get_request_object(level_number: int) -> requests.Session:
    req = requests.session()
    req.auth = (f"natas{level_number}", get_password(level_number))
    return req


def is_secret_correct(current_level_number: int, secret: str) -> bool:
    if len(secret) != password_length and current_level_number != 0:
        return False

    req = requests.session()
    req.auth = (f"natas{current_level_number + 1}", secret)
    result = req.get(get_level_url(current_level_number + 1))
    return result.status_code == 200


def store_secret(current_level_number: int, secret: str) -> None:
    with open(f"{secrets_folder}/natas{current_level_number + 1}.txt", "w") as file:
        file.write(secret)


def store_secret_and_print_message(current_level_number: int, secret: str) -> None:
    if is_secret_correct(current_level_number, secret):
        store_secret(current_level_number, secret)
        print(f"natas{current_level_number} done")
        print(f"secret is {secret}")
    else:
        print(f"natas{current_level_number} failed")
