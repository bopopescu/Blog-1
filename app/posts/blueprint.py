from flask import Blueprint
from flask import render_template

from models import Post, Tag

from flask import request
from .forms import PostForm
from app import db

from flask import redirect
from flask import url_for

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
def create_post():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        posts = Post.query.order_by(Post.created.desc())
    return render_template('posts/index.html', posts=posts)


@posts.route('/<slug>')
def post_details(slug):
    post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post_details.html', post=post)
