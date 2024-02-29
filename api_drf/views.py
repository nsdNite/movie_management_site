from rest_framework import viewsets

from api_drf.pagination import (
    ActorPagination,
    DirectorPagination,
    MoviePagination,
)
from api_drf.serializers import (
    ActorSerializer,
    ActorDetailSerializer,
    ActorListSerializer,
    DirectorListSerializer,
    DirectorDetailSerializer,
    DirectorSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSerializer,
)
from movie_service.models import Actor, Director, Movie


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    pagination_class = ActorPagination

    def get_serializer_class(self):
        if self.action == "list":
            return ActorListSerializer

        if self.action == "retrieve":
            return ActorDetailSerializer

        return ActorSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    pagination_class = DirectorPagination

    def get_serializer_class(self):
        if self.action == "list":
            return DirectorListSerializer

        if self.action == "retrieve":
            return DirectorDetailSerializer

        return DirectorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    pagination_class = MoviePagination

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer

        return MovieSerializer
