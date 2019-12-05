from flask_wtf import FlaskForm
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
    
<<<<<<< HEAD
    submit = SubmitField('Login')

=======
    submit = SubmitField('Login')
>>>>>>> ead650357f12d65c4c2b4a543d0780ea888a908b
