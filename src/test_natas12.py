import os

from config import secrets_folder, assets_folder
from natas12 import get_secret
from utils import is_secret_correct


def test_natas12_php_exists():
    assert os.path.exists(f"{assets_folder}/natas12.php")


def test_natas12_txt_exists():
    assert os.path.exists(f"{secrets_folder}/natas12.txt")


def test_natas12_secret_is_correct():
    assert is_secret_correct(12, get_secret())
