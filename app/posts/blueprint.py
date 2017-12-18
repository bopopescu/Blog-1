from flask import Blueprint
from flask import render_template
from models import Post, Tag
from flask import request
from .forms import PostForm

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create')
def create_post():
    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)


@posts.route('/<slug>')
def post_details(slug):
    post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post_details.html', post=post)
