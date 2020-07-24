import os


def setDefaultEnvironment():
    HOST_USERNAME = os.getenv('HOST_USERNAME')

    if HOST_USERNAME is not None:
        settings = 'base.settings.prod'
    else:
        settings = 'base.settings.dev'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
