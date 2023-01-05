import os

from config import secrets_folder
from natas28 import get_secret
from utils import is_secret_correct


def test_natas28_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas28.txt")


def test_natas28_secret_is_correct():
    assert is_secret_correct(28, get_secret())
