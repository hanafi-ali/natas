import os

from config import secrets_folder
from natas0 import get_secret
from utils import is_secret_correct


def test_natas0_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas0.txt")


def test_natas0_secret_is_correct():
    assert is_secret_correct(0, get_secret())
