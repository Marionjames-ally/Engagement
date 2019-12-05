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
    return render_template('index.html')

@main.route('/admin')
def admin():
    '''
    view root page function that returns thee index and its data
    '''
    title = 'admins portal'  
    
    return render_template('admin.html', title=title)

@main.route('/parent/<int:id>', methods = ['GET','POST'])
def parent():
    '''
    view root page function that returns the index and its data
    ''' 
    
    form = commentForm()
    if form.validate_on_submit():
        body=form.body.data
        
        new_comment=Comment(body=body,posted_by=current_user.username,parent_id=id)
        
        new_comment.save_comment()
        
        return redirect(url_for('.comments', id=id))
    
    title = 'parent portal' 
    comments=Comment.get_comments(id)   
    
    return render_template('parent.html', title=title,comments=comments,form=form)
