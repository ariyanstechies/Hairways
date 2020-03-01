# -*- coding: utf-8 -*-
from django.contrib import admin
from visits.models import Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = ['visitor_hash', 'uri', 'object_app', 'object_model', 'object_id', 'visits']
    list_filter = ['object_app']
    search_fields = ['object_app', 'object_model', 'object_id', 'uri']

admin.site.register(Visit, VisitAdmin)
