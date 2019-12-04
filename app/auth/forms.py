from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User








class LoginForm(FlaskForm):
  email = StringField("Your Email Address",validators=[Required(),Email()])
    password = PasswordField("Password",validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField("Sign In")