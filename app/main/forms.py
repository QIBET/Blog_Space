
from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, StringField, SubmitField,
                     TextAreaField, ValidationError)
from wtforms.validators import Email, EqualTo, Required


class BlogForm(FlaskForm):
    title_blog = StringField('Blog Title', validators= [Required()])
    description = TextAreaField('Blog Body', validators = [Required()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    title_blog = StringField('Blog Title', validators= [Required()])
    description = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField()


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [Required()])
    submit = SubmitField('Submit')

