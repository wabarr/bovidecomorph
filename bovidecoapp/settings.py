"""
Django settings for bovidecoapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import secrets

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = secrets.DEBUG
DEV = secrets.DEV

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['bovids.are-awesome.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bovidecoapp',
    #'axes',
    'tastypie',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'axes.middleware.FailedLoginMiddleware',
)

ROOT_URLCONF = 'bovidecoapp.urls'

WSGI_APPLICATION = 'bovidecoapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if DEV:
    dbPath = "/Users/wabarr/Desktop/bovidecomorph.db"
else:
    dbPath = "/home/wabarr/bovidecomorph.db"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': dbPath,
    }
}

#default URL for user logins (used by @requires_permission() decorator)
LOGIN_URL = "/admin/"


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [os.path.join(BASE_DIR,'templates')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

if not DEV:
    STATIC_ROOT = "/home/wabarr/webapps/bovidecomorph_static/"
else:
    STATIC_ROOT = "/Users/wab536/Desktop/bovid_static"

AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_TEMPLATE = "login_locked.html"
AXES_LOCKOUT_URL = "/lockout/"

# If True, lock out / log based on an IP address AND a user agent.
# This means requests from different user agents but from the same IP are treated differently
AXES_USE_USER_AGENT = True
