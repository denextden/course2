from flask import Blueprint, render_template, request
import logging
from utils import get_comments_by_post_id, get_post_by_pk

post_blueprint = Blueprint('post_blueprint', __name__)


@post_blueprint.route('/posts/<int:pk>')
def post(pk):
    post_by_id = get_post_by_pk(pk)
    commentaries = get_comments_by_post_id(pk)
    len_comments = len(commentaries)
    return render_template('post.html', post_by_id=post_by_id, commentaries=commentaries, len_comments=len_comments)

