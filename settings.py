# Django settings for testapp project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os

ADMINS = (
    ('Pavel Zhukov', 'gelios@gmail.com'),
)

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pybbm',
        'HOST': 'localhost',
        'PASSWORD': 'django',
        'USER': 'django',
        'TEST_CHARSET': 'UTF8',

        }
}
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'en-US'
#USE_I18N = True
SITE_ID = 1

MEDIA_ROOT = ''
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/media/static/'

LOGIN_REDIRECT_URL = '/profile/edit/'

ADMIN_MEDIA_PREFIX = '/media/static/admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pybb.middleware.PybbMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'pybb',
    'pytils',
    'account',
    'sorl.thumbnail',
    'south',
    'pure_pagination',
    'captcha',
    'pinax_theme_bootstrap_account',
    'pinax_theme_bootstrap',
    'django_forms_bootstrap',
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
    'pybb.context_processors.processor',
)

AUTH_PROFILE_MODULE = 'pybb.Profile'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

PYBB_ATTACHMENT_ENABLE = True
ACCOUNT_ACTIVATION_DAYS = 1

PYBB_TEMPLATE = "site_base.html"

import warnings
warnings.filterwarnings(
    'error', r"DateTimeField received a naive datetime",
    RuntimeWarning, r'django\.db\.models\.fields')

ACCOUNT_OPEN_SIGNUP = True

try:
    from settings_local import *
except ImportError:
    pass

import sys
if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_database.sqlite'
    }

