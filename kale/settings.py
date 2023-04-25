import os
from datetime import timedelta
from pathlib import Path
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4kmwdm80^8162poac9wbu_yesbhn3uhpd(uzcaeke_ewt5&*3q'
TEMPLATES_DIRS = (os.path.join(BASE_DIR, 'templates'),)
# SECURITY WARNING: don't run with debug turned on in production!
# import environ
# env = environ.Env()
# env.read_env(str(BASE_DIR / ".env"))
# DEBUG = env.bool("DEBUG", True)
# CACHE_TIME = 84600
# settings.configure()
# ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["*"])
ALLOWED_HOSTS = ['*']
DEBUG = True
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:3000",
    "http://localhost:3030",
    "http://127.0.0.1:9000",
    'http://localhost:5173',
    'http://localhost:5174',
    'http://localhost:5175',
    'http://localhost:5172',
    'http://localhost:5172',
]
BOT_TOKEN = '6297432745:AAE4FSv-KU5Ury2cuAJ5mwQvY-yMFiuM4vs'
GROUP_CHAT_ID = '-1001867869015'
CACHES = {
    'default': {
        'BACKEND':
            'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'cache/abba_kale_cache/caches',
    }
}
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000
CACHE_TIME = 10
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'basic_app',
    'rest_framework',
    'rest_auth',
    'django_cleanup',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_filters'
]
APPEND_SLASH = True
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=259200),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=518400),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE':
        'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
username = 'kaleapi'
password = 'kaleapi'
ROOT_URLCONF = 'kale.urls'
AUTH_USER_MODEL = 'basic_app.CustomUser'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',

    ],
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 3600,  # cache timeout in seconds
    'DEFAULT_CACHE_BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 5

}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIRS,
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
WSGI_APPLICATION = 'kale.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES["default"] = env.db("DATABASE_URL") if DEBUG is False else DATABASES['default']


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

# if DEBUG is False:
#     import logging
#     import sentry_sdk
#     from sentry_sdk.integrations.django import DjangoIntegration
#     from sentry_sdk.integrations.logging import LoggingIntegration
#
#     LOGGING = {
#         "version": 1,
#         "disable_existing_loggers": True,
#         "formatters": {
#             "verbose": {
#                 "format": "%(levelname)s %(asctime)s %(module)s "
#                           "%(process)d %(thread)d %(message)s"
#             }
#         },
#         "handlers": {
#             "console": {
#                 "level": "DEBUG",
#                 "class": "logging.StreamHandler",
#                 "formatter": "verbose",
#             }
#         },
#         "root": {"level": "INFO", "handlers": ["console"]},
#         "loggers": {
#             "django.db.backends": {
#                 "level": "ERROR",
#                 "handlers": ["console"],
#                 "propagate": False,
#             },
#             # Errors logged by the SDK itself
#             "sentry_sdk": {"level": "ERROR", "handlers": ["console"], "propagate": False},
#             "django.security.DisallowedHost": {
#                 "level": "ERROR",
#                 "handlers": ["console"],
#                 "propagate": False,
#             },
#         },
#     }
#     SENTRY_DSN = env("SENTRY_DSN")
#     SENTRY_LOG_LEVEL = env.int("DJANGO_SENTRY_LOG_LEVEL", logging.INFO)
#
#     sentry_logging = LoggingIntegration(
#         level=SENTRY_LOG_LEVEL,  # Capture info and above as breadcrumbs
#         event_level=logging.ERROR,  # Send errors as events
#     )
#     integrations = [
#         sentry_logging,
#         DjangoIntegration(),
#     ]
#     sentry_sdk.init(
#         dsn=SENTRY_DSN,
#         integrations=integrations,
#         environment=env("SENTRY_ENVIRONMENT", default="production"),
#         traces_sample_rate=env.float("SENTRY_TRACES_SAMPLE_RATE", default=0.0),
#     )


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
#
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') if DEBUG else env("DJANGO_STATIC")
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media') if DEBUG else env("DJANGO_MEDIA")

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
