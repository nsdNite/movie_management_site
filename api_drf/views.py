from rest_framework import viewsets

from api_drf.serializers import (
    ActorSerializer,
    ActorDetailSerializer,
    ActorListSerializer,
)
from movie_service.models import Actor


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ActorListSerializer

        if self.action == "retrieve":
            return ActorDetailSerializer

        return ActorSerializer
