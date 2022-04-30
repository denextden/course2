import pytest
from app import app
from utils import get_posts_all


def test_posts_all():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list


def test_keys():
    response = app.test_client().get('/api/posts')
    keys_list = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    test_data = response.json
    for post in test_data:
        if post.keys() in keys_list:
            assert set(post.keys()) == set(keys_list)
