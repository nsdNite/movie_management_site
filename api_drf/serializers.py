from rest_framework import serializers

from movie_service.models import Actor, Director, Movie


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    directors = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = Movie
        fields = ["id", "title", "release_date", "actors", "directors"]


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ["id", "name"]


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ["id", "name"]


class ActorDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ["id", "name", "movies"]


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ["id", "name"]
