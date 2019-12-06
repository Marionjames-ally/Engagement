import os

class Config:
    pass
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProdConfig(Config):
    # pass
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    # pass
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://faith:456789@localhost/engagement'

    DEBUG =True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
    