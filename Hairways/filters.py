from django.contrib.auth.models import User
import django_filters
from .models import Salons


class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Salons
        fields = ['location']
