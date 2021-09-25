import os

class Config:
    pass

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'gradwftformsecret'

config_options = {
'development':DevConfig,
'production':ProdConfig
}