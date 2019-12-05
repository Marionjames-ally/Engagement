from flask import render_template, flash,request,url_for,redirect
from flask_login import login_user,logout_user,login_required
from . import auth
from .forms import LoginForm,RegistrationForm
from ..models import User
from sqlalchemy.testing.config import db

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
    
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email= login_form.email.data).first()
    
        login_user(user,login_form.remember.data)
        return redirect(request.args.get('next') or url_for('main.index'))
    
    flash('Invalid username or password')
    
    title = 'login'
    return render_template('auth/login.html',login_form=login_form,title='login')


@auth.route('/parents_register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
    
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/parents_register.html',registration_form = form)

@auth.route('/parents_login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email= login_form.email.data).first()
    
        login_user(user,login_form.remember.data)
        return redirect(request.args.get('next') or url_for('main.index'))
    
    flash('Invalid username or password')
    title = 'login'
    return render_template('auth/parents_login.html',login_form=login_form,title='login')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))