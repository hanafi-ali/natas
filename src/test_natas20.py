import os

from config import secrets_folder
from natas20 import get_secret
from utils import is_secret_correct


def test_natas20_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas20.txt")


def test_natas20_secret_is_correct():
    assert is_secret_correct(20, get_secret())
