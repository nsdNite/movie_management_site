from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from movie_service.filters import MovieFilter, ActorFilter, DirectorFilter
from movie_service.forms import MovieForm, ActorForm, DirectorForm
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
    """View for handling GET requests for Movie."""

    model = Movie
    filter_class = MovieFilter

    def get(self, request, pk=None):
        if pk:
            movie = get_object_or_404(self.model, id=pk)
            context = {
                "movie": movie,
            }
            return render(request, "movie_service/movie_detail.html", context)
        else:
            f = self.filter_class(
                request.GET, queryset=self.model.objects.all()
            )
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
            form = self.form_class
        return render(request, "movie_service/movie_form.html", {"form": form})


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
        movie = get_object_or_404(self.model, pk=pk)
        form = self.form_class(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect(
                reverse("movie_service:movie-detail", kwargs={"pk": movie.pk})
            )
        else:
            form = self.form_class
        return render(request, "movie_service/movie_form.html", {"form": form})


class MovieDeleteView(View):
    """View for deleting movie."""

    model = Movie

    def post(self, request, pk):
        movie = get_object_or_404(self.model, pk=pk)
        movie.delete()

        return redirect("movie_service:movie-list")


class MovieDeleteConfirmationView(View):
    """View to display delete confirmation page for movie."""

    model = Movie
    template_name = "movie_service/movie_confirm_delete.html"

    def get(self, request, pk):
        movie = get_object_or_404(self.model, id=pk)
        context = {
            "movie_id": pk,
            "movie": movie,
        }

        return render(request, self.template_name, context)


class MovieCancelDeleteView(View):
    """View to handle cancellation of delete operation for movie."""

    def get(self, request):
        return redirect("movie_service:movie-list")


class ActorBaseView(View):
    """View for handling GET requests for Actor."""

    model = Actor
    filter_class = ActorFilter

    def get(self, request, pk=None):
        if pk:
            actor = get_object_or_404(self.model, id=pk)
            context = {
                "actor": actor,
            }
            return render(request, "movie_service/actor_detail.html", context)
        else:
            f = self.filter_class(
                request.GET, queryset=self.model.objects.all()
            )
            filtered_actors = f.qs

            page_number = request.GET.get("page")
            paginator = Paginator(filtered_actors, 25)
            actors_paginated = paginator.get_page(page_number)

            context = {"actors": actors_paginated, "filter": f}
            return render(request, "movie_service/actor_list.html", context)


class ActorCreateView(View):
    """View for creating new actor."""

    model = Actor
    form_class = ActorForm
    template_name = "movie_service/actor_update.html"

    def get(self, request):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_service:actor-list")
        else:
            form = self.form_class
        return render(request, "movie_service/actor_form.html", {"form": form})


class ActorUpdateView(View):
    """View to update the actor name"""

    model = Actor
    form_class = ActorForm
    template_name = "movie_service/actor_update.html"

    def get(self, request, pk):
        actor = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=actor)
        context = {"form": form, "actor": actor}

        return render(request, self.template_name, context)

    def post(self, request, pk):
        actor = get_object_or_404(self.model, pk=pk)
        form = self.form_class(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect(
                reverse("movie_service:actor-detail", kwargs={"pk": actor.pk})
            )
        else:
            form = self.form_class
        return render(request, "movie_service/actor_form.html", {"form": form})


class ActorDeleteView(View):
    """View for deleting actor."""

    model = Actor

    def post(self, request, pk):
        actor = get_object_or_404(self.model, pk=pk)
        actor.delete()

        return redirect("movie_service:actor-list")


class ActorDeleteConfirmationView(View):
    """View to display delete confirmation page for actor."""

    model = Actor
    template_name = "movie_service/actor_confirm_delete.html"

    def get(self, request, pk):
        actor = get_object_or_404(self.model, id=pk)
        context = {
            "actor": actor,
        }

        return render(request, self.template_name, context)


class ActorCancelDeleteView(View):
    """View to handle cancellation of delete operation for actor."""

    def get(self, request):
        return redirect("movie_service:actor-list")


class DirectorBaseView(View):
    """View for handling GET requests for Director."""

    model = Director
    filter_class = DirectorFilter

    def get(self, request, pk=None):
        if pk:
            director = get_object_or_404(self.model, id=pk)
            context = {
                "director": director,
            }
            return render(
                request, "movie_service/director_detail.html", context
            )
        else:
            f = self.filter_class(
                request.GET, queryset=self.model.objects.all()
            )
            filtered_directors = f.qs

            page_number = request.GET.get("page")
            paginator = Paginator(filtered_directors, 25)
            directors_paginated = paginator.get_page(page_number)

            context = {"directors": directors_paginated, "filter": f}
            return render(request, "movie_service/director_list.html", context)


class DirectorCreateView(View):
    """View for creating new director."""

    model = Director
    form_class = DirectorForm
    template_name = "movie_service/director_update.html"

    def get(self, request):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_service:director-list")
        else:
            form = self.form_class
        return render(
            request, "movie_service/director_form.html", {"form": form}
        )


class DirectorUpdateView(View):
    """View to update the director name"""

    model = Director
    form_class = DirectorForm
    template_name = "movie_service/director_update.html"

    def get(self, request, pk):
        director = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=director)
        context = {"form": form, "director": director}

        return render(request, self.template_name, context)

    def post(self, request, pk):
        director = get_object_or_404(self.model, pk=pk)
        form = self.form_class(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return redirect(
                reverse(
                    "movie_service:director-detail", kwargs={"pk": director.pk}
                )
            )
        else:
            form = self.form_class
        return render(request, self.template_name, {"form": form})


class DirectorDeleteView(View):
    """View for deleting director."""

    model = Director

    def post(self, request, pk):
        director = get_object_or_404(self.model, pk=pk)
        director.delete()

        return redirect("movie_service:director-list")


class DirectorDeleteConfirmationView(View):
    """View to display delete confirmation page for director."""

    model = Director
    template_name = "movie_service/director_confirm_delete.html"

    def get(self, request, pk):
        director = get_object_or_404(self.model, id=pk)
        context = {
            "director": director,
        }

        return render(request, self.template_name, context)


class DirectorCancelDeleteView(View):
    """View to handle cancellation of delete operation for director."""

    def get(self, request):
        return redirect("movie_service:director-list")
