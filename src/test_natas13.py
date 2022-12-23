import os

from config import secrets_folder, assets_folder
from natas13 import get_secret
from utils import is_secret_correct


def test_natas13_php_exists():
    assert os.path.exists(f"{assets_folder}/natas13.php")


def test_natas13_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas13.txt")


def test_natas13_secret_is_correct():
    assert is_secret_correct(13, get_secret())
