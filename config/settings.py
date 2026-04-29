# import os
# import dj_database_url
# from pathlib import Path
# from datetime import timedelta

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Security
# SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-your-secret-key-change-in-production')
# DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# # ALLOWED_HOSTS = os.environ.get(
# #     'ALLOWED_HOSTS', 
# #     '.vercel.app,localhost,127.0.0.1,front-memora.vercel.app'
# # ).split(',')
# ALLOWED_HOSTS = ['*', '.vercel.app', 'localhost', '127.0.0.1']

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
    
#     'rest_framework',
#     'rest_framework_simplejwt',
#     'rest_framework_simplejwt.token_blacklist',
#     'corsheaders',
#     'django_filters',
#     'taggit',
    
#     'accounts',
#     'cards',
#     'pet',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'config.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'config.wsgi.application'

# # Database
# # Приоритет отдается DATABASE_URL из переменных окружения
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get('DATABASE_URL', f'sqlite:///{BASE_DIR / "db.sqlite3"}'),
#         conn_max_age=600,
#         conn_health_checks=True,
#     )
# }

# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
# ]

# # Internationalization
# LANGUAGE_CODE = 'ru-ru'
# TIME_ZONE = 'Europe/Moscow'
# USE_I18N = True
# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Cache
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'OPTIONS': {'MAX_ENTRIES': 500},
#     },
# }
# CACHE_TAGS_TTL = 300
# CACHE_STATS_TTL = 120

# AUTH_USER_MODEL = 'accounts.User'

# # CORS & CSRF Settings
# # CORS_ALLOWED_ORIGINS: Здесь протокол https:// ОБЯЗАТЕЛЕН
# CORS_ALLOWED_ORIGINS = os.environ.get(
#     'CORS_ALLOWED_ORIGINS',
#     'http://localhost:3000,http://localhost:5173,http://127.0.0.1:3000,'
#     'https://memora-r0392qk0q-dashas-projects-16d425a3.vercel.app,'
#     'https://front-memora.vercel.app'
# ).split(',')

# CORS_ALLOW_CREDENTIALS = True

# # ВАЖНО: пока бэк на http, эти параметры должны быть False
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# # Позволяет браузеру отправлять данные между разными доменами (Vercel -> Localhost)
# CSRF_COOKIE_SAMESITE = 'Lax'
# SESSION_COOKIE_SAMESITE = 'Lax'

# # Добавляем доверенные источники для CSRF (нужно для POST/PUT запросов)
# CSRF_TRUSTED_ORIGINS = [
#     'https://front-memora.vercel.app',
#     'https://memora-r0392qk0q-dashas-projects-16d425a3.vercel.app',
# ]

# # Django REST Framework
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 50,
#     'DEFAULT_FILTER_BACKENDS': [
#         'django_filters.rest_framework.DjangoFilterBackend',
#     ],
#     'EXCEPTION_HANDLER': 'config.exceptions.custom_exception_handler',
#     'DEFAULT_THROTTLE_CLASSES': [
#         'rest_framework.throttling.AnonRateThrottle',
#         'rest_framework.throttling.UserRateThrottle',
#     ],
#     'DEFAULT_THROTTLE_RATES': {
#         'anon': '100/hour',
#         'user': '1000/hour',
#     },
# }

# # Simple JWT
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
#     'UPDATE_LAST_LOGIN': True,
#     'ROTATE_REFRESH_TOKENS': True,
#     'AUTH_HEADER_TYPES': ('Bearer',),
# }
import os
import dj_database_url
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-me-in-production')

# DEBUG должен быть False в продакшене
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Разрешаем все хосты для Vercel, чтобы не было ошибок 400
ALLOWED_HOSTS = ['*', '.vercel.app', 'localhost', '127.0.0.1']

# --- APPLICATION DEFINITION ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'django_filters',
    'taggit',
    'whitenoise.runserver_nostatic', # Важно для статики
    
    # Your apps
    'accounts',
    'cards',
    'pet',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Сразу после SecurityMiddleware
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls' # Убедись, что папка проекта называется config

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

WSGI_APPLICATION = 'config.wsgi.application'

# --- DATABASE (SUPABASE) ---
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('POSTGRES_URL') or f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# --- AUTH & USER ---
AUTH_USER_MODEL = 'accounts.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
]

# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# --- STATIC & MEDIA ---
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Настройки WhiteNoise для эффективного сжатия статики
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- CORS & CSRF (CRITICAL FOR VERCEL) ---
CORS_ALLOW_ALL_ORIGINS = True # Для разработки можно оставить True, или настрой список ниже:

# Если хочешь строгий список:
# CORS_ALLOWED_ORIGINS = [
#     "https://front-memora.vercel.app",
#     "http://localhost:5173",
# ]

CORS_ALLOW_CREDENTIALS = True

IS_PRODUCTION = os.environ.get('DJANGO_ENV') == 'production'

SESSION_COOKIE_SECURE = IS_PRODUCTION
CSRF_COOKIE_SECURE = IS_PRODUCTION
SESSION_COOKIE_SAMESITE = 'Lax' if IS_PRODUCTION else None
CSRF_COOKIE_SAMESITE = 'Lax' if IS_PRODUCTION else None
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = False # Перенаправлять на HTTPS
APPEND_SLASH = False

CSRF_TRUSTED_ORIGINS = [
    'https://front-memora.vercel.app',
    'https://*.vercel.app', # Разрешаем все поддомены vercel
]

# --- REST FRAMEWORK & JWT ---
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}