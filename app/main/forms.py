
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators= [Required()])
    description = TextAreaField('Blog Body', validators = [Required()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    description = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField()

class UpvoteForm(FlaskForm):
    submit = SubmitField()

class DownvoteForm(FlaskForm):
    submit = SubmitField()
