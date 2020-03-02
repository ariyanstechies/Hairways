# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.aggregates import Max, Min, Avg
from django.utils.translation import ugettext_lazy as _
from visits.utils import is_ignored, gen_hash
from visits import settings

try:
    from django.utils.timezone import now
except ImportError:
    from datetime import datetime
    now = datetime.now

MAX = 1
AVG = 2
MIN = 3


class VisitManager(models.Manager):
    def get_uri_visits_for(self,
                           request,
                           app_model=None,
                           uri=None,
                           regex=None):
        if uri:
            return self.filter(visitor_hash=gen_hash(request, uri),
                               uri=uri,
                               ip_address=request.META.get('REMOTE_ADDR', ''))

        elif app_model:
            return self.filter(object_app=app_model._meta.app_label,
                               object_model=app_model.__class__.__name__,
                               uri__regex="^(.*/){1,}")
        elif regex:
            return self.filter(visitor_hash=gen_hash(request, uri),
                               uri__regex=regex,
                               ip_address=request.META.get('REMOTE_ADDR', ''))

        else:
            raise ValueError(
                'You must pass either of "app_model", "uri" or "regex" parameters.'
            )

    def get_object_visits_for(self, app_model=None, obj=None):
        if obj:
            return self.filter(object_app=obj._meta.app_label,
                               object_model=obj.__class__.__name__,
                               object_id=obj.id)
        elif app_model:
            return self.filter(object_app=app_model._meta.app_label,
                               object_model=app_model.__name__)
        else:
            raise ValueError(
                'You must pass either of "app_model" or "obj" parameters.')

    def add_uri_visit(self, request, uri, app_label):
        visitor_hash = gen_hash(request, uri)
        if settings.VISITS_OBJECTS_AS_COUNTERS:
            visit = self.get_or_create(ip_address=request.META.get(
                'REMOTE_ADDR', ''),
                                       visitor_hash=visitor_hash,
                                       uri=uri,
                                       object_app=app_label)
        else:
            visit = (Visit(ip_address=request.META.get('REMOTE_ADDR', ''),
                           visitor_hash=visitor_hash,
                           uri=uri,
                           object_app=app_label), True)

        if len(visit):
            visit[0].last_visit = Visit.objects.filter(
                visitor_hash=visitor_hash).aggregate(
                    last_visit=models.Max('last_visit'))['last_visit']
            if not is_ignored(request, visit[0]):
                visit[0].last_visit = now()
                visit[0].visits += 1
                visit[0].save()

    def add_object_visit(self, request, obj):
        visitor_hash = gen_hash(request, obj._meta.app_label,
                                obj.__class__.__name__, obj.id)
        if settings.VISITS_OBJECTS_AS_COUNTERS:
            visit = self.get_or_create(visitor_hash=visitor_hash,
                                       object_app=obj._meta.app_label,
                                       object_model=obj.__class__.__name__,
                                       object_id=obj.id,
                                       ip_address=request.META.get(
                                           'REMOTE_ADDR', ''))
        else:
            visit = (Visit(visitor_hash=visitor_hash,
                           object_app=obj._meta.app_label,
                           object_model=obj.__class__.__name__,
                           object_id=obj.id,
                           ip_address=request.META.get('REMOTE_ADDR',
                                                       '')), True)

        if len(visit):
            visit[0].last_visit = Visit.objects.filter(
                visitor_hash=visitor_hash).aggregate(
                    last_visit=models.Max('last_visit'))['last_visit']
            if not is_ignored(request, visit[0]):
                visit[0].last_visit = now()
                visit[0].visits += 1
                visit[0].save()

    def calculate(self, obj, uri, what=MAX):
        if obj:
            visits = self.filter(object_app=obj._meta.app_label,
                                 object_model=obj.__class__.__name__)
        elif uri:
            visits = self.filter(uri=uri).aggregate(Max("visits"))
        else:
            raise Exception("Parameters obj or uri must be specified")

        if what is MAX:
            return visits.aggregate(Max("visits"))
        elif what is MIN:
            return visits.aggregate(Min("visits"))
        elif what is AVG:
            return visits.aggregate(Avg("visits"))
        else:
            return None


class Visit(models.Model):
    visitor_hash = models.CharField(max_length=40,
                                    blank=True,
                                    null=True,
                                    db_index=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True,
                                              null=True,
                                              db_index=True)
    last_visit = models.DateTimeField(blank=True, null=True)
    visits = models.IntegerField(default=0)
    object_app = models.CharField(max_length=255)
    object_model = models.CharField(max_length=255)
    object_id = models.CharField(max_length=255)
    blocked = models.BooleanField(default=False)

    objects = VisitManager()

    def __unicode__(self):
        return self.visitor_hash

    def __str__(self):
        return str(self.visits)

    class Meta:
        app_label = "visits"
        ordering = ('uri', 'object_model', 'object_id')
        verbose_name = _('visit')
        verbose_name_plural = _('visits')
