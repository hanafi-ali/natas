import os

from config import secrets_folder
from natas24 import get_secret
from utils import is_secret_correct


def test_natas24_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas24.txt")


def test_natas24_secret_is_correct():
    assert is_secret_correct(24, get_secret())
