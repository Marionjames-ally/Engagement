from flask import render_template,redirect,url_for,request,abort
from . import main
from app import db 
from .. import db
from ..models import User,Admin,Parent,Comment
from .forms import commentForm
import datetime
from flask_login import login_required,current_user

@main.route('/')
def index():
    '''
    function that retuns the index
    '''
    title = 'school'
    return render_template('index.html',current_user=current_user)


@main.route('/admin')
@login_required
def admin():
    '''
    view root page function that returns thee index and its data
    '''
    title = 'admin portal'  
    
    return render_template('admin.html', title=title)

@main.route('/parent')
@login_required
def parent():
    '''
    view root page function that returns the index and its data
    '''
    title = 'parent portal'    
    
    return render_template('admin.html')

@main.route('/comments/', methods=['GET','POST'])
@login_required
def comments():
    
    form = commentForm()
    
    if form.validate_on_submit():
        body=form.body.data
        
        new_comment=Comment(body=body,posted_by=current_user.username,user_id=current_user.id)
        
        new_comment.save_comment()        
        return redirect(url_for('main.comments'))
    
    comments=Comment.get_comments()
    return render_template('comments.html',comments=comments,form=form)

@main.route('/photos')
def photos():
    
    return render_template('photos.html')

@main.route('/gallery')
def gallery():
    
    return render_template('gallery.html')

@main.route('/about')
def about():
    
    return render_template('about.html')
