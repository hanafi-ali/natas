import os

from config import secrets_folder
from natas8 import get_secret
from utils import is_secret_correct


def test_natas8_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas8.txt")


def test_natas8_secret_is_correct():
    assert is_secret_correct(8, get_secret())
