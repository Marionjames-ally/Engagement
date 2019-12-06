from flask import render_template 
from . import main
# from app import db 
# from .. import db
# from ..models import User


@main.route('/')
def index():
    '''
    function that retuns the index
    '''
    
    title = 'school'
    return render_template('index.html')

@main.route('/admin')
def admin():
 return render_template('admin.html')
    