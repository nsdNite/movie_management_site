from django.contrib import admin

from movie_service.models import Actor, Director, Movie

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Movie)
