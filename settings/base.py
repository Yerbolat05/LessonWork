import os
import sys
from settings.conf import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
SECRET_KEY = ' cfkpknpwlzo8+9imu*6!g!+92vqaio0&c-cy+xgm3!wk_$o^)+'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Application definition
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR,'apps'))

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_extensions',

]

PROJECT_APPS = [
    'firstapp.apps.FirstappConfig',
    'abstracts.apps.AbstractsConfig',
    'auths.apps.AuthsConfig',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

AUTH_USER_MODEL = 'auths.CustomUser'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
ROOT_URLCONF = 'urls.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

ADMIN_SITE_URLS = 'yerbo05/'


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

DEBUG_TOOLBAR_PANELS = [ 
    'debug_toolbar.panels.versions.VersionsPanel', 
    'debug_toolbar.panels.timer.TimerPanel', 
    'debug_toolbar.panels.settings.SettingsPanel', 
    'debug_toolbar.panels.headers.HeadersPanel', 
    'debug_toolbar.panels.request.RequestPanel', 
    'debug_toolbar.panels.sql.SQLPanel', 
    'debug_toolbar.panels.staticfiles.StaticFilesPanel', 
    'debug_toolbar.panels.templates.TemplatesPanel', 
    'debug_toolbar.panels.cache.CachePanel', 
    'debug_toolbar.panels.signals.SignalsPanel', 
    'debug_toolbar.panels.logging.LoggingPanel', 
    'debug_toolbar.panels.redirects.RedirectsPanel', 
]

INTERNAL_IPS = [ 
    "127.0.0.1", 
]

SHELL_PLUS_PRE_IMPORTS = [ 
    ('django.db', ('connection', 'reset_queries', 'connections')), 
    ('datetime', ('datetime', 'timedelta', 'date')), 
    ('json', ('loads', 'dumps')), 
] 
SHELL_PLUS_MODEL_ALIASES = { 
    'university': { 
        'Student': 'S', 
        'Account': 'A', 
        'Group': 'G', 
        'Professor': 'P', 
    }, 
} 
SHELL_PLUS = 'Ipython' 
SHELL_PLUS_PRINT_SQL = True 
SHELL_PLUS_PRINT_SQL_TRUNCATE = 1000
