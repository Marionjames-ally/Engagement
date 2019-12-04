from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    function that returns the views
    '''
    title = 'School'
    return render_template('index.html', title=title)