import json


from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt


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


class MovieListViewFront(View):
    def get(self, request):
        movies_list = Movie.objects.all()
        paginator = Paginator(movies_list, 25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "movies": page_obj,
        }
        return render(request, "movie_service/movie_list.html", context)


class MovieDetailViewFront(View):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        context = {"movie": movie}
        return render(request, "movie_service/movie_detail.html", context)

    @csrf_exempt
    def post(self, request, pk):
        data = json.loads(request.body)
        movie = get_object_or_404(Movie, pk=pk)

        movie.title = data.get("title", movie.title)
        movie.release_year = data.get("release_year", movie.release_year)
        movie.director = data.get("director", movie.director)
        movie.plot = data.get("plot", movie.plot)
        movie.save()

        return JsonResponse({"message": "Movie updated successfully"})

    @csrf_exempt
    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return JsonResponse({"message": "Movie deleted successfully"})
