import os

from config import secrets_folder
from utils import is_secret_correct, get_password


def test_natas19_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas19.txt")


def test_natas19_secret_is_correct():
    assert is_secret_correct(19, get_password(20))
