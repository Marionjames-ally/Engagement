from flask import render_template 
from . import main


@main.route('/')
def index():
    '''
    function that retuns the index
    '''
    
    title = 'school'
    return render_template('index.html')
    