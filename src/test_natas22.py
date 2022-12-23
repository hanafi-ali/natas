import os

from config import secrets_folder
from natas22 import get_secret
from utils import is_secret_correct


def test_natas22_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas22.txt")


def test_natas22_secret_is_correct():
    assert is_secret_correct(22, get_secret())
