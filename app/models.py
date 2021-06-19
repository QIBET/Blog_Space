from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager 
from datetime import datetime 

@login_manager.user_loader
def load_user(user_id):
    return Writer.query.get(int(user_id))




class Writer(UserMixin,db.Model):
    '''
    models that defines properties of user class
    '''
    __tablename__="writers"

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(),unique = True,index = True)
    password_hash=db.Column(db.String(255)) 
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('PitchComments', backref = 'user', lazy = 'dynamic')
    upvotes = db.relationship('Upvote', backref = 'user', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise ArithmeticError('You cannnot read the password attribute')
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
     
        
    def __repr__(self):
        return f'User {self.username}'