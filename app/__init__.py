from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from config import Config
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.loginview = 'auth.login'


bootstrap=Bootstrap()

def create_app(config_name):
    
    app = Flask(__name__)
    
    #creting app configs
    app.config.from_object(Config)
    app.config.from_object(config_options[config_name])
    
    #initializing flask extension
    bootstrap.init_app(app)
    
    #registering blueprint
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')
    
    return app