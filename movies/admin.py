from django.contrib import admin

from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['comment', 'movie', 'user', 'reported']
    list_filter = ['reported']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)

