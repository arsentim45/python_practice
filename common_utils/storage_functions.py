import os
import random


def get_download_dir(search_keyword):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(base_dir, search_keyword.replace(' ', '-').lower())
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
    return download_dir


def get_random_name():
    random_int = str(random.randrange(1000, 10000))
    return f'{random_int}.jpg'