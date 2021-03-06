from flask import render_template,request,redirect,abort
from flask.helpers import url_for
from . import main
from ..models import User,BlogPost,Comments
from .forms import BlogPostsForm,UpdateProfile,CommentForm
from .. import db,photos
from flask_login import login_required
from flask_login import login_required, current_user
from ..requests import quotes

@main.route('/')
def index():
    display_quotes = quotes()
    title="Home"
    return render_template("index.html",title=title,display_quotes=display_quotes)

@main.route("/posts/new", methods = ["GET","POST"])
@login_required
def new_posts():
    form = BlogPostsForm()
    if form.validate_on_submit():
        new_blogpost = BlogPost(title = form.title.data,content = form.blog_post.data,author=form.author.data,user = current_user)
        new_blogpost.save_blogposts()
        return redirect(url_for("main.new_posts"))

    title="post"
    post = BlogPost.get_blogposts()
    return render_template("new_blogpost.html",title=title,BlogPostForm=form,post = post)

@main.route('/deleteblogpost/<int:id>',methods = ['GET','DELETE'])
@login_required
def delete_blogpost(id): 
  blogpost = BlogPost.query.filter_by(id = id).first()
  if blogpost: 
    db.session.delete(blogpost)
    db.session.commit()
  else: 
    abort(404)
  return redirect(url_for('.new_blogpost'))

@main.route('/comments/<int:id>',methods = ['GET','POST'])
# 
def new_comment(id): 
    form = CommentForm()
    blogposts = BlogPost.query.filter_by(id = id).first()
    if blogposts is None: 
        abort(404) 
    print(blogposts)
    if form.validate_on_submit(): 
        new_comment = Comments(comment = form.comment.data,user=current_user,blogpost_id = id)
        new_comment.save_comment()

    comments_available = Comments.get_comments(id)
    title = 'comments'
    return render_template('comments.html', title = title, comments_form = form, blogposts = blogposts,comments_available = comments_available)

@main.route('/deletecomment/<int:id>',methods = ['GET','DELETE'])
@login_required
def delete_comment(id):
    comment = Comments.query.filter_by(id = id).first()
    if comment: 
        db.session.delete(comment)
        db.session.commit()
    else: 
        abort(404)
    return redirect(url_for('/comments', id = comment.blogpost_id))


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

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))







