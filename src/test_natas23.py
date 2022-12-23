import os

from config import secrets_folder
from natas23 import get_secret
from utils import is_secret_correct


def test_natas23_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas23.txt")


def test_natas23_secret_is_correct():
    assert is_secret_correct(23, get_secret())
