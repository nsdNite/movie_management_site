from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from movie_api_test import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("movie_service.urls"), name="movie_service"),
    path("api/", include("api_drf.urls"), name="api_drf"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
