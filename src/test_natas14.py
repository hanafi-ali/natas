import os

from config import secrets_folder
from natas14 import get_secret
from utils import is_secret_correct


def test_natas14_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas14.txt")


def test_natas14_secret_is_correct():
    assert is_secret_correct(14, get_secret())
