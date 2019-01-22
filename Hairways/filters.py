from django.contrib.auth.models import User
import django_filters
from .models import 

class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Location
        fields = ['location']