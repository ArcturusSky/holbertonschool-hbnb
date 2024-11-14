import os

class Config:
    """
    Base configuration class with default settings.

    Attributes:
        SECRET_KEY (str): Secret key for cryptographic operations, retrieved from the environment variable 'SECRET_KEY'.
                          If not set, defaults to 'default_secret_key'.
        DEBUG (bool): Indicates whether to enable debug mode. Default is False.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    JWT_SECRET_KEY = SECRET_KEY
    DEBUG = False

class DevelopmentConfig(Config):
    """
    Development-specific configuration.

    Inherits from the base Config class and overrides the DEBUG setting to enable debugging.
    """
    DEBUG = True

class ProductionConfig(Config):
    """
    Production-specific configuration.

    Because when in production the Debugmode shouldn't be on
    """
    DEBUG = False

class TestingConfig(Config):
    """
    Configuration meants for all testing.
    """
    TESTING = True


# Dictionary to manage different configurations based on environment.
config = {
    'development': DevelopmentConfig,  # Configuration for development environment
    'default': DevelopmentConfig       # Default configuration (set to development in this case)
}
