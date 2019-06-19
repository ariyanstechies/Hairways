import os
import dj_database_url
from dotenv import load_dotenv
load_dotenv(verbose=True)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Hairways',
    'crispy_forms',
    #'social_django',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# #   GOOGLE FACEBOOK OAUTH
# AUTHENTICATION_BACKENDS = (
#  'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
#  'social_core.backends.google.GoogleOpenId',  # for Google authentication
#  'social_core.backends.google.GoogleOAuth2',  # for Google authentication
#  'social_core.backends.github.GithubOAuth2',  # for Github authentication
#  'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication
#
#  'django.contrib.auth.backends.ModelBackend',
# )

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='937755655618-iff20mdr7vkk0mp73s8gbpegrvlu9hnv.apps.googleusercontent.com'  # client Id
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'N2yMghmefwhS1lrny32qAqcN' # client secret

ROOT_URLCONF = 'Base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Hairways/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #cial_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'Base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# do necessary configuration for Heroku.

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'Hairways.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# user redirected to home after successfull login
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# prints emails on the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Hairways/static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
