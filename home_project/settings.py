# by Richi Rod AKA @richionline / falken20
# TODO: Tag all the files with the copyright

import os
from dotenv import load_dotenv  # Manage environment vars in .env file
import dj_database_url  # For returning a Django database connection dictionary


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Looking for .env file for environment vars
load_dotenv(os.path.join(BASE_DIR, '.env'), override=True)

SECRET_KEY = os.getenv('SECRET_KEY')

# Heroku is a server web for running the app
HEROKU = ('ENV' in os.environ and os.environ['ENV'] == 'PRO')

print(f'ROD --> ENV: {HEROKU}')

if 'DEBUG' in os.environ:
    DEBUG = os.getenv('DEBUG')
else:
    DEBUG = not HEROKU

print(f'ROD --> DEBUG: {DEBUG}')

# SECURITY WARNING: don't run with debug turned on in production!
if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['falken-home.herokuapp.com']

# print('ROD vars\n DEBUG: %s\n ALLOWED_HOSTS: %s' % (format(DEBUG), format(ALLOWED_HOSTS)))
print(f'ROD --> ALLOWED_HOSTS: {ALLOWED_HOSTS}')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Apps
    'app_english_dic',
    'app_home',
    'app_todo',
    'app_books',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'home_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # ROD
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

WSGI_APPLICATION = 'home_project.wsgi.application'

DATABASES = {
    'secondary': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'falken_homedb',
        'USER': 'falken_home',
        'PASSWORD': '(Falken_home-33)',
        'HOST': 'localhost',
        'PORT': '',
    },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

# In production environment (in this case Heroku) it is necessary to change the DB url
if HEROKU:
    DATABASES['default'] = dj_database_url.config(default=os.getenv('DATABASE_URL'))

print(f'ROD --> DATABASES: {DATABASES["default"]}')

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

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
# ROD: About django.contrib.staticfiles installed apps
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
