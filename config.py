# App configs are defined here. To switch app config, set the environment variable
# FLASK_CONFIG to the wanted one.

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'some secret key')


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
        'default': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        }
