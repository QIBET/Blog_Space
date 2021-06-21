from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager 
from datetime import datetime 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(UserMixin,db.Model):
    '''
    models that defines properties of user class
    '''
    __tablename__="users"

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(),unique = True,index = True)
    password_hash=db.Column(db.String(255)) 
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    
    @property
    def password(self):
        raise ArithmeticError('You cannnot read the password attribute')
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
     
        
    def __repr__(self):
        return f'Writer {self.username}'
class Blog(db.Model):
    '''
    properties of blog class
    '''
    __tablename__='blogs' 

    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    title=db.Column(db.String(255))
    category=db.Column(db.String(255))
    description=db.Column(db.String())
    date_posted=db.Column(db.DateTime,default=datetime.utcnow)
    comments = db.relationship('Comment',backref='blog',lazy='dynamic')
    

    @classmethod
    def get_blogs(cls, id):
        blogs = Blog.query.order_by(blog_id=id).desc().all()    
        return blogs

    def __repr__(self):
        return f'Blog {self.description}'

class Comment(db.Model):
    '''
    model that defines the properties of comments
    '''
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)
    pitch_id=db.Column(db.Integer,db.ForeignKey("blogs.id"),nullable= False)
    description=db.Column(db.String())
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"),nullable= False)
    date_posted=db.Column(db.DateTime,default=datetime.utcnow)

    def save_blogs(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls,id):
        blogs = Comment.query.filter_by(pitch_id = id).all()
        return blogs

    def __repr__(self):
        return f'{self.pitch_id}:{self.pitch_id}'
