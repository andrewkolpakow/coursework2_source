import pytest
from utils import *


def test_get_posts_all():
    posts = get_posts_all(path='posts.json')
    assert len(posts) != 0

def test_get_posts_by_user():
    posts = get_posts_by_user('leo')
    assert len(posts) != 0
