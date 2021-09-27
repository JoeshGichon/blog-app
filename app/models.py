from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy.orm import backref

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    blogpost = db.relationship('BlogPost',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comments',backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class BlogPost(db.Model):
    __tablename__ = 'blogpost'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    author = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comments',backref = 'blogpost', lazy = "dynamic")

    def save_blogposts(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogposts(cls):
        blogpost = BlogPost.query.all()
        return blogpost

    def __repr__(self): 
        return f'BlogPost {self.id} > {self.content}'

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    author = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)


    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blogpost_id = db.Column(db.Integer,db.ForeignKey('blogpost.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(blogpost_id = id).all()
        return comments
  
    def __repr__(self): 
        return f'Comment {self.blogpost_id} > {self.comment}'

class Quotes:
  def __init__(self,author,quote):
    self.author = author
    self.quote = quote

