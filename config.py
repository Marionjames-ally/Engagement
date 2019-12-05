<<<<<<< HEAD
import os 

class Config:
    pass
    
=======
import os

class Config:
    pass
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

>>>>>>> gakori
class ProdConfig(Config):
    pass

class DevConfig(Config):
<<<<<<< HEAD
    
    DEBUG=True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
=======
    # pass
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://faith:456789@localhost/engagement'

    DEBUG =True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
>>>>>>> gakori
}
    