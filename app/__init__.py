from flask import Flask
from flask_login import LoginManager
from config import Config_options



login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(Config_options[config_name])

    # initialize flask extention
    login_manager.init_app(app)