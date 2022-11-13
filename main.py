from flask import Flask, render_template, request, jsonify

from logger import get_logger
from utils import *
import logging

app = Flask(__name__)
logger = get_logger("main")

@app.route("/", methods=['GET'])
def all_posts():
    posts = get_posts_all()
    logger.info("knock knock")
    return render_template('index.html', posts=posts)
'''View for the index page with all the posts'''


@app.route("/post/<int:pk>", methods=['GET'])
def get_post(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)
'''View with post by pk and appropriate comments'''


@app.route("/search")
def search_page():
    query = request.args.get('s')
    posts = search_for_posts(query)
    len_posts = len(posts)
    return render_template('search.html', posts=posts, query=query, len_posts=len_posts)
'''View for the search page'''

@app.route("/user/<user_name>")
def post_by_user(user_name):
    posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts, substr=user_name)
'''View for the posts by user_name'''


@app.route("/api/posts")
def get_posts_api():
    posts = get_posts_all()
    return jsonify(posts)
'''API which shows all the posts in json format'''


@app.route("/api/posts/<int:pk>")
def get_post_api(pk):
    post_found = get_post_by_pk(pk)
    return jsonify(post_found)
'''API which shows the certain post by pk in json format'''


@app.errorhandler(404)
def not_found(e):
    return "404 page not found"


@app.errorhandler(500)
def server_error(e):
    return "500 internal server error"


app.run(debug=True)
