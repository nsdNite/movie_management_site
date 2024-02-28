from django.urls import path

from movie_service.views import (
    IndexView,
    MovieView,
    MovieDeleteView,
    MovieUpdateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("movies/", MovieView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieView.as_view(), name="movie-detail"),
    path("movies/new/", MovieView.as_view(), name="movie-new"),
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
]

app_name = "movie_service"
