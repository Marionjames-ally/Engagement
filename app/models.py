from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f'User {self.username}'