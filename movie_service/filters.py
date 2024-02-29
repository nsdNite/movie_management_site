import django_filters
from django.db.models.functions import ExtractYear


from movie_service.models import Movie, Actor, Director


class ActorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains"
    )

    class Meta:
        model = Actor
        fields = ["name"]


class DirectorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains"
    )

    class Meta:
        model = Director
        fields = ["name"]


class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name="title", lookup_expr="icontains"
    )
    release_date = django_filters.CharFilter(
        field_name="release_date", method="filter_release_year"
    )
    directors = django_filters.CharFilter(
        field_name="directors__name",  # Assuming "name" is the field on directors
        lookup_expr="icontains",
    )
    actors = django_filters.CharFilter(
        field_name="actors__name",  # Assuming "name" is the field on actors
        lookup_expr="icontains",
    )

    class Meta:
        model = Movie
        fields = ["title", "release_date", "directors", "actors"]

    def filter_release_year(self, queryset, name, value):
        if value:
            try:
                year = int(value)
                return queryset.annotate(
                    year=ExtractYear("release_date")
                ).filter(year=year)
            except ValueError:
                return queryset.none()
        return queryset
