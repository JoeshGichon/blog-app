import os

class Config:
    debug = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

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