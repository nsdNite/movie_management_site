from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from movie_api_test import settings
from movie_service.views import IndexView, MovieListView, MovieDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("movie_service.urls", namespace="api")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
