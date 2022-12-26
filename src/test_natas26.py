import os

from config import secrets_folder, assets_folder
from natas26 import get_secret
from utils import is_secret_correct


def test_natas26_php_exists():
    assert os.path.exists(f"{assets_folder}/natas26.php")


def test_natas26_serialized_txt_exists():
    assert os.path.exists(f"{assets_folder}/natas26_serialized.txt")


def test_natas26_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas26.txt")


def test_natas26_secret_is_correct():
    assert is_secret_correct(26, get_secret())
