import os

class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass

    DEBUG =True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
    