from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%2rhsy87%z-)sjdytuu)v@7u81=z_z8=k)9i(y@#dm@t!dxq2('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'outdoorvibrations.herokuapp.com']


EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'c938d5dce08ab3'
EMAIL_HOST_PASSWORD = 'b19de5f6f83ae7'
EMAIL_PORT = '2525'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog.apps.BlogConfig',

    'bootstrap5',

    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    "whitenoise.middleware.WhiteNoiseMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'outdoorvibrations.urls'

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

WSGI_APPLICATION = 'outdoorvibrations.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'outdoorvibrations',
        'USER': 'cesarjaramillo',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'outdoorvibrations-identifier.cndahqtfgjmk.us-west-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}

# import dj_database_url

# DATABASES['default'] = dj_database_url.config(
#     conn_max_age=600,
#     conn_health_checks=True,
# )


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
   BASE_DIR / 'blog/static',
]

MEDIA_ROOT = BASE_DIR / 'blog/static/blog/images'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL =  '/images/'

# AWS S3 Bucket
AWS_QUERYSTRING_AUTH = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'outdoorvibrations-bucket'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if os.getcwd() == '/app':
    DEBUG = False