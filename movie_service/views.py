from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from movie_service.filters import MovieFilter
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


class MovieBaseView(View):
    """A base view for handling GET requests."""

    def get(self, request, pk=None):
        if pk:
            movie = get_object_or_404(Movie, id=pk)
            context = {
                "movie": movie,
            }
            return render(request, "movie_service/movie_detail.html", context)
        else:
            f = MovieFilter(request.GET, queryset=Movie.objects.all())
            filtered_movies = f.qs

            page_number = request.GET.get("page")
            paginator = Paginator(filtered_movies, 25)
            movies_paginated = paginator.get_page(page_number)

            context = {"movies": movies_paginated, "filter": f}
            return render(request, "movie_service/movie_list.html", context)


class MovieCreateView(View):
    """View for creating new movie."""

    model = Movie
    form_class = MovieForm
    template_name = "movie_service/movie_update.html"

    def get(self, request):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_service:movie-list")
        else:
            form = MovieForm()
        return render(request, "movie_service/movie_form.html", {"form": form})
        # form = self.form_class(request.POST)
        #
        # if form.is_valid():
        #     title = form.cleaned_data["title"]
        #     release_date = form.cleaned_data["release_date"]
        #     director_names = form.cleaned_data["directors"].split(",")
        #     actors_names = form.cleaned_data["actors"].split(",")
        #
        #     directors = []
        #     for director_name in director_names:
        #         director, created = Director.objects.get_or_create(
        #             name=director_name,
        #         )
        #         directors.append(director)
        #
        #     actors = []
        #     for actor_name in actors_names:
        #         actor, created = Actor.objects.get_or_create(
        #             name=actor_name,
        #         )
        #         actors.append(actor)
        #
        #     movie = Movie.objects.create(
        #         title=title,
        #         release_date=release_date,
        #     )
        #
        #     movie.directors.set(directors)
        #     movie.actors.set(actors)
        #
        #     movie.save()
        #
        #     return redirect("movie_service:movie-list")
        #
        # context = {"form": form}
        # return render(request, self.template_name, context)


class MovieDeleteView(View):
    """View for deleting movie."""

    model = Movie

    def post(self, request, pk):
        movie = get_object_or_404(self.model, pk=pk)
        movie.delete()

        return redirect("movie_service:movie-list")


class DeleteConfirmationView(View):
    """View to display delete confirmation page."""

    template_name = "movie_service/movie_confirm_delete.html"

    def get(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        context = {
            "movie_id": pk,
            "movie": movie,
        }

        return render(request, self.template_name, context)


class CancelDeleteView(View):
    """View to handle cancellation of delete operation."""

    def get(self, request):
        return redirect("movie_service:movie-list")


class MovieUpdateView(View):
    """View to update the movie details"""

    model = Movie
    form_class = MovieForm
    template_name = "movie_service/movie_update.html"

    def get(self, request, pk):
        movie = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=movie)
        context = {"form": form, "movie": movie}

        return render(request, self.template_name, context)

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = self.form_class(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect(
                reverse("movie_service:movie-detail", kwargs={"pk": movie.pk})
            )
        else:
            form = MovieForm()
        return render(request, "movie_service/movie_form.html", {"form": form})

        # movie = get_object_or_404(self.model, pk=pk)
        # form = self.form_class(request.POST, instance=movie)
        #
        # if form.is_valid():
        #     title = form.cleaned_data["title"]
        #     release_date = form.cleaned_data["release_date"]
        #     director_names = form.cleaned_data["directors"].split(",")
        #     actors_names = form.cleaned_data["actors"].split(",")
        #
        #     directors = []
        #     for director_name in director_names:
        #         director, created = Director.objects.get_or_create(
        #             name=director_name,
        #         )
        #         directors.append(director)
        #
        #     actors = []
        #     for actor_name in actors_names:
        #         actor, created = Actor.objects.get_or_create(
        #             name=actor_name,
        #         )
        #         actors.append(actor)
        #
        #     movie.title = title
        #     movie.release_date = release_date
        #     movie.directors.set(directors)
        #     movie.actors.set(actors)
        #     movie.save()
        #
        #     return redirect("movie_service:movie-list")

        # context = {"form": form, "movie": movie}
        #
        # return render(request, self.template_name, context)
