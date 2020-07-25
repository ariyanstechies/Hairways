from base.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# EMAILS
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
