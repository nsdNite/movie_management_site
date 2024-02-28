from django.urls import path

from movie_service.views import (
    IndexView,
    MovieBaseView,
    MovieDeleteView,
    DeleteConfirmationView,
    CancelDeleteView,
    MovieUpdateView,
    MovieCreateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("movies/", MovieBaseView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieBaseView.as_view(), name="movie-detail"),
    path("movies/create/", MovieCreateView.as_view(), name="movie-create"),
    path(
        "movies/<int:pk>/delete/",
        MovieDeleteView.as_view(),
        name="movie-delete",
    ),
    path(
        "movies/<int:pk>/delete/confirm/",
        DeleteConfirmationView.as_view(),
        name="delete-confirmation",
    ),
    path(
        "movies/delete/cancel/",
        CancelDeleteView.as_view(),
        name="cancel-delete",
    ),
    path(
        "movies/<int:pk>/update/",
        MovieUpdateView.as_view(),
        name="movie-update",
    ),
]

app_name = "movie_service"
