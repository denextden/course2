from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from post.post import post_blueprint
from search.search import search_blueprint
from user_post.user_post import user_post_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_post_blueprint)

app.run(debug=True)
