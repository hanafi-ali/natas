import os

from config import secrets_folder
from natas6 import get_secret
from utils import is_secret_correct


def test_natas6_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas6.txt")


def test_natas6_secret_is_correct():
    assert is_secret_correct(6, get_secret())
