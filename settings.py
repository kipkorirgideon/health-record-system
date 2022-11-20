from pathlib import Path
import os
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY', default='')
DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'records',
    'allauth',
    'allauth.account',
    'bootstrap5',
    'simple_history',
    'algoliasearch_django',
    'django_tables2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware'
]

ROOT_URLCONF = 'urls'

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
                'django_settings_export.settings_export',
            ],
        },
    },
]

AUTH_USER_MODEL = "accounts.User"
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SIGNUP_REDIRECT_URL = "/dashboard/"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {
    'login': 'accounts.forms.CustomLoginForm',
    'signup': 'accounts.forms.CustomSignupForm',
}

WSGI_APPLICATION = 'wsgi.application'

BOOTSTRAP5 = {
    'required_css_class': 'field-required',
}

DATABASES = {
    'default': env.db(),
}

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'django_static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SETTINGS_EXPORT = [
    'ALGOLIA_APPLICATION_ID',
    'ALGOLIA_SUFFIX',
    'ALGOLIA_PUBLIC_KEY',
]

ALGOLIA_APPLICATION_ID = env.str('ALGOLIA_APPLICATION_ID', default='')
ALGOLIA_API_KEY = env.str('ALGOLIA_API_KEY', default='')
ALGOLIA_SUFFIX = env.str('ALGOLIA_SUFFIX', default='')
ALGOLIA_PUBLIC_KEY = env('ALGOLIA_PUBLIC_KEY', default='')
ALGOLIA = {
    'APPLICATION_ID': ALGOLIA_APPLICATION_ID,
    'API_KEY': ALGOLIA_API_KEY,
    'INDEX_SUFFIX': ALGOLIA_SUFFIX,
    'AUTO_INDEXING': True,
    'RAISE_EXCEPTIONS': False
}
