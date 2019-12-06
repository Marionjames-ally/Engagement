from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.loginview = 'auth.login'

bootstrap = Bootstrap()
csrf=CSRFProtect()
db = SQLAlchemy()

def create_app(config_name):
    
    app= Flask(__name__)

    #create app configs
    app.config.from_object(Config)
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY']='d686414d5eeb7d38df7e8c385b2c2c47'
    
    #initializing
    bootstrap.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    #registering
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')
    
    return app