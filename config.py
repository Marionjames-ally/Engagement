import os

class Config:
    
    pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    pass
    DEBUG = True
    
Config_options = {
'development':DevConfig,
'production':ProdConfig,

}
   
