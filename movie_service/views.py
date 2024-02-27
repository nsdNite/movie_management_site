from django.shortcuts import render
from django.views.generic import View

from movie_service.models import Movie, Actor, Director


# Create your views here.


class IndexView(View):
    template_name = "movie_api_test/index.html"

    def get(self, request, *args, **kwargs):
        num_movie = Movie.objects.count()
        num_actors = Actor.objects.count()
        num_directors = Director.objects.count()

        num_visits = request.session.get("num_visits", 0)
        request.session["num_visits"] = num_visits + 1

        context = {
            "num_movie": num_movie,
            "num_actors": num_actors,
            "num_directors": num_directors,
            "num_visits": num_visits + 1,
        }

        return render(request, self.template_name, context=context)
