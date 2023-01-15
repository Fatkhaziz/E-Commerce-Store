from .models import Goods
from django_filters import FilterSet


class ProductFilter(FilterSet):
    class Meta:
        model = Goods
        fields = ['name', 'category', 'price']