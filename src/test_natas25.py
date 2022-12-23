import os

from config import secrets_folder
from natas25 import get_secret
from utils import is_secret_correct


def test_natas25_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas25.txt")


def test_natas25_secret_is_correct():
    assert is_secret_correct(25, get_secret())
