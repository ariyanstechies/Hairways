from django.core.wsgi import get_wsgi_application

from base.settings import conf

conf.setDefaultEnvironment()
application = get_wsgi_application()
