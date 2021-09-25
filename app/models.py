from . import db

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

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'