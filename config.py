from sqlalchemy import create_engine

class Config(object):
    DEGUB = False
    TESTING = False
    CSRF_ENABLE = True
    SECRET_KEY = 'something super secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fbeuser:fbepassword@localhost:5432/fbe'

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
