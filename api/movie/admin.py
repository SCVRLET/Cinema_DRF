from django.contrib import admin

from .models import Movie, Person, MovieGenre, Serial


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'world_premier', 'duration_in_minutes')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')


@admin.register(MovieGenre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = ('name', 'world_premier', 'budget_in_dollars')

