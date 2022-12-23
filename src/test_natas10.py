import os

from config import secrets_folder
from natas10 import get_secret
from utils import is_secret_correct


def test_natas10_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas10.txt")


def test_natas10_secret_is_correct():
    assert is_secret_correct(10, get_secret())
