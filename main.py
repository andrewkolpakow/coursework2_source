from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/", methods=['GET'])
def all_posts():
    all_posts = get_posts_all()
    return render_template('index.html', all_posts=all_posts)


app.run(debug=True)