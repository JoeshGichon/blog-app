from flask import render_template,request,redirect
from flask.helpers import url_for
from . import main
from ..models import BlogPost
from .forms import BlogPostsForm

@main.route('/')
def index():
    title="Home"
    return render_template("index.html",title=title)

@main.route("/posts/new", methods = ["GET","POST"])
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





