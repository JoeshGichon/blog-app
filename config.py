import os

class Config:
    debug = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'gradwftformsecret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'

config_options = {
'development':DevConfig,
'production':ProdConfig
}