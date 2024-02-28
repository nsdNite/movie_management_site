from datetime import datetime


from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    class Meta:
        ordering = ("first_name",)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Director(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ("first_name",)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    director = models.ManyToManyField(Director, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")

    class Meta:
        ordering = ("title",)

    def __str__(self) -> str:
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
                if " " in director_names:
                    first_name, last_name = director_name.split(" ", 1)
                else:
                    first_name = director_name
                    last_name = ""
                director, created = Director.objects.get_or_create(
                    first_name=first_name, last_name=last_name
                )
                director_objs.append(director)

        actor_objs = []
        for actor_name in actor_names:
            print(actor_name)
            if actor_name:
                if " " in actor_name:
                    first_name, last_name = actor_name.split(" ", 1)
                else:
                    first_name = actor_name
                    last_name = ""
                actor, created = Actor.objects.get_or_create(
                    first_name=first_name, last_name=last_name
                )
                actor_objs.append(actor)

        movie = cls.objects.create(title=title, release_date=release_date)
        movie.director.set(director_objs)
        movie.actors.set(actor_objs)
        return movie
