from flask import Flask, request, render_template, send_from_directory, jsonify
from utils import get_posts_all, get_post_by_pk
from main.main import main_blueprint
from post.post import post_blueprint
from search.search import search_blueprint
from user_post.user_post import user_post_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_post_blueprint)


@app.route('/api/posts')
def get_posts_json():
    posts_json = []

    for post in get_posts_all():
        posts_json.append(post)

    return jsonify(posts_json)


@app.route('/api/posts/<int:post_id>')
def get_post_json(post_id):
    post = get_post_by_pk(post_id)

    return jsonify(post)


if __name__ == '__main__':
    app.run(debug=True)
