import json
import requests


from django.core.management.base import BaseCommand

from movie_service.models import Director, Actor, Movie


class Command(BaseCommand):

    def handle(self, *args, **options):
        api_key = "75c3d997"
        response = requests.get(
            "https://www.omdbapi.com/?apikey=75c3d997&s=Avengers"
        )

        url = "http://www.omdbapi.com/?i=tt3896198&apikey=" + api_key

        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            director_names = [
                name.strip() for name in data["Director"].split(",")
            ]
            actors_names = [name.strip() for name in data["Actors"].split(",")]

            director_objs = []
            for director_name in director_names:
                first_name, last_name = director_name.split(" ", 1)
                director, created = Director.objects.get_or_create(
                    first_name=first_name, last_name=last_name
                )
                director_objs.append(director)

            actor_objs = []
            for actor_name in actors_names:
                first_name, last_name = actor_name.split(" ", 1)
                actor, created = Actor.objects.get_or_create(
                    first_name=first_name, last_name=last_name
                )
                actor_objs.append(actor)

            movie = Movie.objects.create(
                title=data["Title"],
                release_date=data["Released"],
            )

            movie.director.set(director_objs)
            movie.actors.set(actor_objs)

            self.stdout.write(
                self.style.SUCCESS("Data imported successfully!")
            )
        else:
            self.stdout.write(
                self.style.ERROR("Failed to import data from OMDB API.")
            )
