import environ
import os
from pathlib import Path
from core.json_loggin_config import CustomJsonFormatter

# Connect environ


env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DOMAIN_NAME = 'http://localhost:8000'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_django',

    'mainapp',
    'productapp',
    'authapp',
    'cartapp',
    'wishapp',
    'orderapp',

]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.vk.VKOAuth2',
)

AUTH_USER_MODEL = 'authapp.User'

# VKAuth
SOCIAL_AUTH_VK_OAUTH2_KEY = env('SOCIAL_AUTH_VK_OAUTH2_KEY')
SOCIAL_AUTH_VK_OAUTH2_SECRET = env('SOCIAL_AUTH_VK_OAUTH2_SECRET')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        "console": {
            "format": "{asctime}-{levelname}-{module}-{filename}-{message}",
            "style": '{',
        },
        'json_formater': {
            '()': CustomJsonFormatter
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'json_formater',
            'filename': './logs/django.log'
        },
        'view_file': {
            'class': 'logging.FileHandler',
            'formatter': 'json_formater',
            'filename': './logs/view.log'
        },

    },

    'loggers': {
        'django_logger': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'view_logger': {
            'handlers': ['view_file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

ROOT_URLCONF = 'mainapp.urls'

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

                'core.context_processors.genders_list',
                'core.context_processors.product_categories',
                'core.context_processors.products',
                'core.context_processors.cart_total_quantity',
                'core.context_processors.get_user_products_in_wishlist',
                'core.context_processors.get_user_orders',
            ],
        },
    },
]

WSGI_APPLICATION = 'mainapp.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('NAME'),
        'USER': env('USER_NAME'),
        'PASSWORD': env('USER_PASSWORD'),
        'HOST': env('HOST'),
        'PORT': env('PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

LOGIN_URL = '/auth/login/'
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# redis settings
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'

# Celery settings
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
