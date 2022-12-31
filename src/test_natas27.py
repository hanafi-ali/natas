import os

from config import secrets_folder
from natas27 import get_secret
from utils import is_secret_correct


def test_natas27_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas27.txt")


def test_natas27_secret_is_correct():
    assert is_secret_correct(27, get_secret())
