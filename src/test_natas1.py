import os

from config import secrets_folder
from natas1 import get_secret
from utils import is_secret_correct


def test_natas1_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas1.txt")


def test_natas1_secret_is_correct():
    assert is_secret_correct(1, get_secret())
