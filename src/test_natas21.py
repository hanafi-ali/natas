import os

from config import secrets_folder
from natas21 import get_secret
from utils import is_secret_correct


def test_natas21_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas21.txt")


def test_natas21_secret_is_correct():
    assert is_secret_correct(21, get_secret())
