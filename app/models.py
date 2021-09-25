from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))

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

class BlogPost:

    all_posts = []

    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author

    def save_post(self):
        BlogPost.all_posts.append(self)

    @classmethod
    def clear_post(cls):
        BlogPost.all_posts.clear()

    @classmethod
    def get_posts(cls):
        response = []
        for post in cls.all_posts:
            response.append(post)
        return response

