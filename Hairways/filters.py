from .models import Salons
import django_filters


class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Salons
        fields = ['location']
