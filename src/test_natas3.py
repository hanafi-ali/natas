import os

from config import secrets_folder
from natas3 import get_secret
from utils import is_secret_correct


def test_natas3_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas3.txt")


def test_natas3_secret_is_correct():
    assert is_secret_correct(3, get_secret())
