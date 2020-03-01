# -*- coding: utf-8 -*-
from visits.utils import gen_hash


def request_meta(request):
    uri = request.META.get("PATH_INFO", None)
    ip = request.META.get('REMOTE_ADDR', '')
    return {
        "visits_meta": {
            "request_path": uri,
            "visitor_hash": gen_hash(request, uri),
            "ip_address": ip,
        }
    }
