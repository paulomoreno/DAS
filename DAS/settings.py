# coding: utf-8

"""
Django settings for DAS project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from pathlib import Path

# caminho completo da raiz do projeto
PROJECT_DIR = Path(__file__).resolve().parents[2]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^f(@_y1+_b+!af)_$l6lfji)116@wvrb=gz%xi8f2c_tn4d1bx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DAS.urls'

WSGI_APPLICATION = 'DAS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Media URL - where to save uploaded media
MEDIA_ROOT = PROJECT_DIR.joinpath('media').as_posix()
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# Caminho que contem os arquivos estaticos
STATIC_ROOT = PROJECT_DIR.joinpath('static').as_posix()
# prefixo da URL para ser usada direta no template, porem nao é recomendavel usar o caminhho direto mas sim "{% static 'url' %}"
STATIC_URL = '/static/' 

# Indicates the local filesystem path for Django to get static files
STATIC_PATH = os.path.abspath(os.path.join(BASE_DIR, 'static'))
STATICFILES_DIRS = (
    STATIC_PATH,
)

# Templates
TEMPLATE_PATH = os.path.abspath(os.path.join(BASE_DIR, 'templates'))
TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)
