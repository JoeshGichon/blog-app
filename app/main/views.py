from flask import render_template,request,redirect,abort
from flask.helpers import url_for
from . import main
from ..models import BlogPost,User
from .forms import BlogPostsForm,UpdateProfile
from .. import db
from flask_login import login_required

@main.route('/')
def index():
    title="Home"
    return render_template("index.html",title=title)

@main.route("/posts/new", methods = ["GET","POST"])
@login_required
def new_posts():
    form = BlogPostsForm()
    if form.validate_on_submit():
        post_title = form.title.data
        post_content = form.blog_post.data
        post_author = form.author.data
        new_post = BlogPost(title=post_title,content=post_content,author=post_author)
        new_post.save_post()
        return redirect(url_for("main.new_posts"))

    title="post"
    post = BlogPost.get_posts()
    return render_template("new_blogpost.html",title=title,BlogPostForm=form,post = post)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update_profile.html',form =form)





