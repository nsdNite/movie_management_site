import os
import requests

from django.core.management.base import BaseCommand

from dotenv import load_dotenv

from movie_service.models import Movie

load_dotenv()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("arg1", type=int, help="Start movie id")
        parser.add_argument("arg2", type=int, help="End movie id")

    def handle(self, *args, **options):
        api_key = os.environ.get("OMDB_API_KEY")
        url_base = "https://www.omdbapi.com/?apikey=" + api_key
        start_id = options["arg1"]
        end_id = options["arg2"]

        movies_processed = 0

        for movie_id in range(start_id, end_id + 1):
            url = f"{url_base}&i=tt00{movie_id}"
            response = requests.get(url)
            data = response.json()

            if data.get("Response") == "True":
                movie = Movie.create_from_api(data)
                if movie is not None:
                    movies_processed += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Processed movie {movies_processed}: {data["Title"]}'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f'Skipped movie {movie_id}: {data["Title"]}'
                        )
                    )
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to import movie tt{movie_id}")
                )

        self.stdout.write(self.style.SUCCESS("Data import complete!"))
