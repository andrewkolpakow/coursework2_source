from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)


@app.route("/", methods=['GET'])
def all_posts():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route("/posts/<int:pk>", methods=['GET'])
def get_post(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    #post_id = pk
    return render_template('post.html', post=post, comments=comments)

@app.route("/search")
def search_page():
    query = request.args.get('s')
    posts = search_for_posts(query)
    len_posts = len(posts)
    return render_template('search.html', posts=posts, query=query, len_posts=len_posts)

@app.route("/users/<user_name>")
def post_by_user(user_name):
    posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts)

app.run(debug=True)