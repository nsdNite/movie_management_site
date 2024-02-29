from datetime import datetime


from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

    def __repr__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    directors = models.ManyToManyField(
        Director, related_name="movies", blank=True
    )
    actors = models.ManyToManyField(Actor, related_name="movies", blank=True)

    class Meta:
        ordering = ("title",)

    def __str__(self) -> str:
        return self.title

    def __repr__(self):
        return self.title

    @property
    def formatted_release_date(self):
        return self.release_date.strftime("%d %b %Y")

    @classmethod
    def create_from_api(cls, api_data):
        title = api_data.get("Title", "")
        raw_release_date = api_data.get("Released", "")

        if raw_release_date == "N/A":
            return None

        try:
            release_date = datetime.strptime(
                raw_release_date, "%d %b %Y"
            ).date()
        except ValueError:
            return None

        director_names = [
            name.strip() for name in api_data.get("Director", "").split(",")
        ]
        actor_names = [
            name.strip() for name in api_data.get("Actors", "").split(",")
        ]

        director_objs = []
        for director_name in director_names:
            if director_name:
                name = director_name
                director, created = Director.objects.get_or_create(
                    name=name,
                )
                director_objs.append(director)

        actor_objs = []
        for actor_name in actor_names:
            if actor_name:

                name = actor_name
                actor, created = Actor.objects.get_or_create(
                    name=name,
                )
                actor_objs.append(actor)

        movie = cls.objects.create(title=title, release_date=release_date)
        movie.directors.set(director_objs)
        movie.actors.set(actor_objs)
        return movie
