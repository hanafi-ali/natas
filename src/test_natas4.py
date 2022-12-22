import os

from config import secrets_folder
from natas4 import get_secret
from utils import is_secret_correct


def test_natas4_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas4.txt")


def test_natas4_secret_is_correct():
    assert is_secret_correct(4, get_secret())
