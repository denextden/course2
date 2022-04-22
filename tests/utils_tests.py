import pytest

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, get_posts_by_user, search_for_posts


def test_get_posts_all():
    posts = get_posts_all()
    assert posts == type(list)
