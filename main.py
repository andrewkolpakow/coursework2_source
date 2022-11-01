from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/", methods=['GET'])
def all_posts():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route("/posts/<int:post_id>")
def get_comments_by_post_id(post_id):
    comment = get_comments_by_post_id(post_id)
    return render_template('post.html', comment=comment)


app.run(debug=True)