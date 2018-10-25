import os
import secrets
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """ This class is used to set the initial configuration
       variables for the app. """
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """ enables development environment """
    DEBUG = True


class TestingConfig(BaseConfig):
    """ enables testing environment """
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False


env_config = dict(
    development=DevelopmentConfig,
    tesing=TestingConfig,
    production=ProductionConfig
    )
