from django.contrib import admin
from .models import Movie, Genre


# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('title', 'number_in_stock', 'daily_rate')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
