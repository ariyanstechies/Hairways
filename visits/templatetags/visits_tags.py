# -*- coding: utf-8 -*-
from django.template import Library, Node, TemplateSyntaxError, Variable
from django.utils.translation import ugettext as _
from django.db.models import Sum, Model

from visits.models import Visit

register = Library()


class VisitsNode(Node):
    def __init__(self, obj, context_var):
        self.obj = Variable(obj)
        self.context_var = context_var

    def render(self, context):
        obj = self.obj.resolve(context)
        if isinstance(obj, str):
            context[self.context_var] = Visit.objects.filter(
                uri__regex=obj, ).aggregate(
                    visits_sum=Sum("visits"))["visits_sum"]
        elif isinstance(obj, dict):
            context[self.context_var] = Visit.objects.filter(
                uri=obj["request_path"], ).aggregate(
                    visits_sum=Sum("visits"))["visits_sum"]
        elif isinstance(obj, Model):
            context[self.context_var] = Visit.objects.filter(
                object_app=obj._meta.app_label,
                object_model=obj.__class__.__name__,
                object_id=obj.id).aggregate(
                    visits_sum=Sum('visits'))['visits_sum']
        else:
            context[self.context_var] = 0

        return ''


def do_get_visits(parser, token):
    """
    Retrive the number of visits of a model/slug
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError(
            _('%s tag requires exactly three arguments') % bits[0])
    if bits[2] != 'as':
        raise TemplateSyntaxError(
            _("second argument to %s tag must be 'as'") % bits[0])
    return VisitsNode(bits[1], bits[3])


register.tag("get_visits", do_get_visits)
