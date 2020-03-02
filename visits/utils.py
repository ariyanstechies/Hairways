# -*- coding: utf-8 -*-
import hashlib
import datetime
from visits import settings

try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.datetime.now


def is_ignored(request, visit, url=True, bots=True, user_agents=True):
    if url:
        for ignored_url in settings.IGNORE_URLS:
            if request.META["PATH_INFO"].startswith(ignored_url):
                return True

    if user_agents:
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        if user_agent in settings.IGNORE_USER_AGENTS:
            return True

        '''try regex matching too'''
        import re
        for ua_pattern in settings.IGNORE_USER_AGENTS:
            if re.search(ua_pattern, user_agent):
                return True

    if bots and request.META.get("IS_BOT", False):
        return True

    if not visit.last_visit:
        return False

    time_since_last_visit = visit.last_visit + datetime.timedelta(minutes=settings.MIN_TIME_BETWEEN_VISITS)

    if time_since_last_visit < now():
        return False
    else:
        return True


def gen_hash(request, *args):
    h = hashlib.sha1()
    for request_field in settings.REQUEST_FIELDS_FOR_HASH:
        h.update(request.META.get(request_field, '').encode('utf-8'))
    for arg in args:
        h.update(str(arg).encode('utf-8'))
    return h.hexdigest()


def get_app_from_object(obj):
    return obj._meta.app_label


def get_model_from_object(obj):
    return obj.__class__.__name__
