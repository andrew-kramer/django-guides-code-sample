"""
Key settings derived from the .env file
"""

import os


class Database:
    """
    Database settings
    """
    NAME = os.getenv('POSTGRES_DB')
    USER = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    HOST = os.getenv('DATABASE_HOST')
    PORT = os.getenv('DATABASE_PORT')


class Secrets:
    """
    Application Secrets
    """
    SECRET_KEY = os.getenv('APPLICATION_KEY', 'SuperSecret')


class Settings:
    """
    Application-level settings
    """
    # Which environment are we running in? Either 'dev' or 'prod'
    APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT', 'prod')

    # Where should the browser point to reach the base of this website? Used, for example, in emails where we can't rely
    # on the browser to have the base URL.
    SITE_DOMAIN = os.getenv('SITE_DOMAIN', 'localhost')
    SITE_NAME = os.getenv('SITE_NAME', 'Django Guides Code Sample')

    EXTERNAL_HOST = os.getenv('EXTERNAL_HOST', None)
    ALLOW_LOCALHOST = (os.getenv('ALLOW_LOCALHOST', "false") == "true")
    EXTRA_LOCALHOST = os.getenv('EXTRA_LOCALHOST', None)


class Email:
    """
    Email settings
    """
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
