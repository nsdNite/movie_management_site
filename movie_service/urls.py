from django.urls import path

from movie_service.views import (
    IndexView,
    MovieDetailViewFront,
    MovieListViewFront,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("movies/", MovieListViewFront.as_view(), name="movie-list"),
    path(
        "movies/<int:pk>/", MovieDetailViewFront.as_view(), name="movie-detail"
    ),
    path(
        "movies/<int:pk>/update/",
        MovieDetailViewFront.as_view(),
        name="movie_update",
    ),
    path(
        "movies/<int:pk>/delete/",
        MovieDetailViewFront.as_view(),
        name="movie_delete",
    ),
]

app_name = "movie_service"
