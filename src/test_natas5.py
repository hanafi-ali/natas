import os

from config import secrets_folder
from natas5 import get_secret
from utils import is_secret_correct


def test_natas5_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas5.txt")


def test_natas5_secret_is_correct():
    assert is_secret_correct(5, get_secret())
