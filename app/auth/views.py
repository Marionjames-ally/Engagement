from . import auth
from flask import flash,render_template,redirect,url_for,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from ..email import mail_message
