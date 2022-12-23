import os

from config import secrets_folder
from natas7 import get_secret
from utils import is_secret_correct


def test_natas7_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas7.txt")


def test_natas7_secret_is_correct():
    assert is_secret_correct(7, get_secret())
