from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from datetime import datetime

class BlogPostsForm(FlaskForm):
    title = StringField('Blog Post title',validators=[Required()])
    blog_post = TextAreaField('Blog Post', validators=[Required()])
    author=StringField("Author", validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
