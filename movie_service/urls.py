from django.urls import path

from movie_service.views import (
    IndexView,
    MovieBaseView,
    MovieDeleteView,
    MovieDeleteConfirmationView,
    MovieCancelDeleteView,
    MovieUpdateView,
    MovieCreateView,
    ActorBaseView,
    ActorCreateView,
    ActorUpdateView,
    ActorDeleteView,
    ActorDeleteConfirmationView,
    ActorCancelDeleteView,
    DirectorBaseView,
    DirectorCreateView,
    DirectorUpdateView,
    DirectorDeleteView,
    DirectorDeleteConfirmationView,
    DirectorCancelDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("movies/", MovieBaseView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieBaseView.as_view(), name="movie-detail"),
    path("movies/create/", MovieCreateView.as_view(), name="movie-create"),
    path(
        "movies/<int:pk>/update/",
        MovieUpdateView.as_view(),
        name="movie-update",
    ),
    path(
        "movies/<int:pk>/delete/",
        MovieDeleteView.as_view(),
        name="movie-delete",
    ),
    path(
        "movies/<int:pk>/delete/confirm/",
        MovieDeleteConfirmationView.as_view(),
        name="movie-delete-confirmation",
    ),
    path(
        "movies/delete/cancel/",
        MovieCancelDeleteView.as_view(),
        name="movie-cancel-delete",
    ),
    path("actors/", ActorBaseView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorBaseView.as_view(), name="actor-detail"),
    path("actors/create/", ActorCreateView.as_view(), name="actor-create"),
    path(
        "actors/<int:pk>/update/",
        ActorUpdateView.as_view(),
        name="actor-update",
    ),
    path(
        "actors/<int:pk>/delete/",
        ActorDeleteView.as_view(),
        name="actor-delete",
    ),
    path(
        "actors/<int:pk>/delete/confirm/",
        ActorDeleteConfirmationView.as_view(),
        name="actor-delete-confirmation",
    ),
    path(
        "actors/delete/cancel/",
        ActorCancelDeleteView.as_view(),
        name="actor-cancel-delete",
    ),
    path("directors/", DirectorBaseView.as_view(), name="director-list"),
    path(
        "directors/<int:pk>/",
        DirectorBaseView.as_view(),
        name="director-detail",
    ),
    path(
        "directors/create/",
        DirectorCreateView.as_view(),
        name="director-create",
    ),
    path(
        "directors/<int:pk>/update/",
        DirectorUpdateView.as_view(),
        name="director-update",
    ),
    path(
        "directors/<int:pk>/delete/",
        DirectorDeleteView.as_view(),
        name="director-delete",
    ),
    path(
        "directors/<int:pk>/delete/confirm/",
        DirectorDeleteConfirmationView.as_view(),
        name="director-delete-confirmation",
    ),
    path(
        "directors/delete/cancel/",
        DirectorCancelDeleteView.as_view(),
        name="director-cancel-delete",
    ),
]


app_name = "movie_service"
