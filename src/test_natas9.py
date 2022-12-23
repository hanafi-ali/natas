import os

from config import secrets_folder
from natas9 import get_secret
from utils import is_secret_correct


def test_natas9_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas9.txt")


def test_natas9_secret_is_correct():
    assert is_secret_correct(9, get_secret())
