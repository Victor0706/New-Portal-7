from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='added_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )


    class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'postCategory': ['exact'],
           'added_at': ['gt'],
       }
