import os

from config import secrets_folder
from natas11 import get_secret
from utils import is_secret_correct


def test_natas11_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas11.txt")


def test_natas11_secret_is_correct():
    assert is_secret_correct(11, get_secret())
