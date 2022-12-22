import os

from config import secrets_folder
from natas2 import get_secret
from utils import is_secret_correct


def test_natas2_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas2.txt")


def test_natas2_secret_is_correct():
    assert is_secret_correct(2, get_secret())
