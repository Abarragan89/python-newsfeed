from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db

#this bp object now has all the routes
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    # get all posts
    db = get_db()
    posts = db.query(Post).order_by(Post.created_at.desc()).all()
    return render_template('homepage.html', posts=posts)

@bp.route('/login')
def login(): 
    return render_template('login.html')

# <id> becomes the parameter in the function
@bp.route('/post/<id>')
def single(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()

    #return single post template
    return render_template('single-post.html', post=post)