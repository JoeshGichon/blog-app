import os

class Config:
    debug = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'gradwftformsecret'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'

config_options = {
'development':DevConfig,
'production':ProdConfig
}