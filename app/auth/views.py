<<<<<<< HEAD
from flask import render_template, flash,request,url_for,redirect
from flask_login import login_user,logout_user,login_required
from . import auth
from .forms import LoginForm,RegistrationForm
from ..models import User
# from sqlalchemy.testing.config import db

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        # db.session.add(user)
        # db.session.commit()
    
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
def parents_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        # db.session.add(user)
        # db.session.commit()
    
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/parents_register.html',registration_form = form)

@auth.route('/parents_login', methods = ['GET', 'POST'])
def parents_login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email= login_form.email.data).first()
    
        login_user(user,login_form.remember.data)
        return redirect(request.args.get('next') or url_for('main.index'))
    
    flash('Invalid username or password')
    title = 'login'
    return render_template('auth/parents_login.html',login_form=login_form,title='login')
=======
from . import auth
from flask import flash,render_template,redirect,url_for,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from ..email import mail_message



@auth.route('/login',methods=['GET','POST'])
def login():
    '''
    View Function to login users
    '''

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return render_template('home.html')

    flash('Invalid username or password !')

    title = "Blog-Up Login"
    return render_template('auth/login.html',login_form = login_form,title = title)



@auth.route('/register',methods = ["GET","POST"])
def register():
    '''
    View Function to register new users
    '''

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("You've been successfully registered!")

        mail_message("Welcome to Blog-Up","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))

    title = "Blog-Up registration"
    return render_template('auth/register.html',registration_form = form, title = title)

>>>>>>> 4fb246d9db5c093755bbcd20e4c85fe5496b7416


@auth.route('/logout')
@login_required
def logout():
<<<<<<< HEAD
    logout_user()
    return redirect(url_for('main.index'))
=======
    '''
    View Function to logout a user
    '''

    logout_user()

    flash("You've been successfully registered!")

    return redirect(url_for("main.index"))
>>>>>>> 4fb246d9db5c093755bbcd20e4c85fe5496b7416
