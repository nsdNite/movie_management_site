from django_filters import rest_framework as filters

from movie_service.models import Movie, Director, Actor


class ActorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")


class DirectorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    release_date = filters.DateFromToRangeFilter()
    directors = filters.ModelMultipleChoiceFilter(
        field_name="directors__name",
        queryset=Director.objects.all(),
        to_field_name="name",
        lookup_expr="icontains",
    )
    actors = filters.ModelMultipleChoiceFilter(
        field_name="actors__name",
        queryset=Actor.objects.all(),
        to_field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = Movie
        fields = ["title", "release_date", "directors", "actors"]
