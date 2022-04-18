from flask import Blueprint, render_template, request
from utils import get_posts_by_user

user_post_blueprint = Blueprint('user_post_blueprint', __name__)


@user_post_blueprint.route('/users/<user_name>')
def user_post(user_name):
    user_posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', user_posts=user_posts)