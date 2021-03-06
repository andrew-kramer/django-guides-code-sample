"""
Django settings

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import sys

from pathlib import Path
from main_app.keyconfig import Database, Secrets, Settings, Email


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = Secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (Settings.APP_ENVIRONMENT == 'dev')


# ALLOWED HOSTS

ALLOWED_HOSTS = []

if Settings.EXTERNAL_HOST:
    ALLOWED_HOSTS.append(Settings.EXTERNAL_HOST)

if Settings.ALLOW_LOCALHOST:
    ALLOWED_HOSTS.append('localhost')
    if Settings.EXTRA_LOCALHOST:
        ALLOWED_HOSTS.append(Settings.EXTRA_LOCALHOST)


INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # Modules
    'allauth',
    'allauth.account',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'rest_framework',
    'corsheaders',
    'webpack_loader',

    # My Apps
    # 'games',
    # 'guides'
]

MIGRATION_MODULES = {
    'sites': 'main_app.migrations.sites',
    # 'account': 'main_app.migrations.allauth.account'
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = (Settings.APP_ENVIRONMENT == 'dev')

ROOT_URLCONF = 'main_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'main_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if 'test' in sys.argv:
    # noinspection PyUnresolvedReferences
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test_database'
        }
    }
else:
    DATABASES = {
        'default': {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": Database.NAME,
            "USER": Database.USER,
            "PASSWORD": Database.PASSWORD,
            "HOST": Database.HOST,
            "PORT": Database.PORT,
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles", "static")
STATICFILES_DIRS = []

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Webpack options

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'frontend/dist/js',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend', 'dist', 'webpack-stats.json')
    }
}

# Security for Cookies and Sessions

# CSRF_COOKIE_SAMESITE = 'Strict'
# SESSION_COOKIE_SAMESITE = 'Strict'
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

# PROD ONLY
# CSRF_COOKIE_SECURE = (Settings.APP_ENVIRONMENT != 'dev')
# SESSION_COOKIE_SECURE = (Settings.APP_ENVIRONMENT != 'dev')


# Email Settings

EMAIL_HOST = Email.EMAIL_HOST
EMAIL_HOST_USER = Email.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = Email.EMAIL_HOST_PASSWORD
EMAIL_PORT = Email.EMAIL_PORT


# REST Framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'django-guides-auth'
JWT_AUTH_REFRESH_COOKIE = 'django-guides-auth-refresh'


# AllAuth

AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend'
]

SITE_ID = 1

if 'test' in sys.argv:
    FIXTURE_DIRS = ['guides/test-fixtures']

