import pytest
from app import app
from utils import get_posts_all, get_post_by_pk


def test_posts_all():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict


def test_keys():
    response = app.test_client().get('/api/posts/1')
    keys_list = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    test_data = response.json
    assert set(test_data.keys()) == set(keys_list)
