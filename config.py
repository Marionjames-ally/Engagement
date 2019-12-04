import os

class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass

    DEBUG =True
    
    confi_options = {
        'development':DevConfig,
        'production':ProdConfi
    }
    