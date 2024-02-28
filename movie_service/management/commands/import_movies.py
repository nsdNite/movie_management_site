import requests

from django.core.management.base import BaseCommand

from movie_service.models import Movie


class Command(BaseCommand):

    def handle(self, *args, **options):
        api_key = "75c3d997"
        url_base = "https://www.omdbapi.com/?apikey=" + api_key
        start_id = 80000
        end_id = 80000 + 100

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
