from flask import Blueprint, render_template, request
from utils import get_posts_all, search_for_posts
search_blueprint = Blueprint('search_blueprint', __name__)


@search_blueprint.route('/search/')
def search():
    search_by_word = request.args['s']
    posts = search_for_posts(search_by_word)
    len_posts = len(posts)

    return render_template('search.html', search_by_word=search_by_word, posts=posts, len_posts=len_posts)

