from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Email,Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('confirm_password')])
    
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()]) 
    
    submit = SubmitField('sign up')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')
=======
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User








class LoginForm(FlaskForm):
  email = StringField("Your Email Address",validators=[Required(),Email()])
    password = PasswordField("Password",validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField("Sign In")
>>>>>>> 4fb246d9db5c093755bbcd20e4c85fe5496b7416
