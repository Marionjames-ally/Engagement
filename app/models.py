from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    '''
    function that queries the database to check if user exists
    '''
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)
    pass_secure = db.Column(db.String(255))
    parent=db.relationship('Parent', backref='Parent', lazy='dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Admin(db.Model):
    __tablename__= 'admin'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    admin_title = db.Column(db.String(255))
    admin_content = db.Column(db.String(5000))
    
    def save_Admin(self):
        db.session.add(self)
        db.session.commit()
        
class Parent(db.Model):
    __tablename__='parent'
    
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    body = db.Column(db.String(5000))
    posted_on=db.Column(db.DateTime,default=datetime.utcnow)
    posted_by=db.Column(db.String(255))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    comment=db.relationship('Comment',backref='comment',lazy='dynamic')
    
    def save_parent(self):
        db.session.add(self)
        db.session.commit()
        
    
class Comment(db.Model):
    __tablename__='comments'
    
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(255))
    posted_by=db.Column(db.String(255))
    posted_on=db.Column(db.DateTime,default=datetime.utcnow)
    parent_id=db.Column(db.Integer,db.ForeignKey('parent.id'))
    
    
    def save_comment(self):
        '''
        function that saves a new comment to the database
        '''
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,id):
        '''
        function that get comments for a parent 
        '''
        comments =  Comment.query.filter_by(parent_id=id).all()
        return comments
    
    def delete_comment(self):
        '''
        function that deletes a comment from database 
        '''
        db.session.delete(self)
        db.session.commit()
        
    def __repr__(self):
        '''
        function that helps in dec=bugging
        '''
        return f'Comment {self.body}'
            
            
            
            
            
            
            
            
            
        
        
    
    