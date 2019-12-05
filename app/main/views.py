<<<<<<< HEAD
from flask import render_template
from . import main
=======
from flask import render_template 
from . import main
# from app import db 
# from .. import db
# from ..models import User

>>>>>>> gakori

@main.route('/')
def index():
    '''
<<<<<<< HEAD
    function that returns the views
    '''
    title = 'School'
    return render_template('index.html', title=title)
=======
    function that retuns the index
    '''
    
    title = 'school'
    return render_template('index.html')
    
>>>>>>> gakori
