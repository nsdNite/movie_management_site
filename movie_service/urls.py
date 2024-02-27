from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from movie_service.views import IndexView, MovieDetailView, MovieListView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
]
