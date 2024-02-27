import json

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import BaseDeleteView, DeleteView, UpdateView

from movie_service.forms import MovieForm
from movie_service.models import Movie, Actor, Director


class IndexView(View):
    template_name = "movie_service/index.html"

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


class MovieView(View):
    def get(self, request, pk=None):
        if pk:
            movie = get_object_or_404(Movie, id=pk)
            context = {
                "movie": movie,
            }
            return render(request, "movie_service/movie_detail.html", context)
        else:
            movies = Movie.objects.all()
            context = {
                "movies": movies,
            }
            return render(request, "movie_service/movie_list.html", context)


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy("movie_service:movie-list")
    template_name = "movie_service/movie_confirm_delete.html"


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ["title", "release_date", "director", "actors"]
    success_url = reverse_lazy("movie_service/movie-list")
