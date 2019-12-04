from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, StringField, SubmitField,ValidationError)
from wtforms.validators import Email, EqualTo, Required

