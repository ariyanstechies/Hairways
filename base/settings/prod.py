from base.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# For extra security --run python manage.py check --deploy
 
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True


ALLOWED_HOSTS = ['.hairwayskenya.com']

# TODO ADD SENTRY 


# Static
STATIC_ROOT = os.path.join(BASE_DIR,
                           f'/home/{HOST_USERNAME}/hairways/static')