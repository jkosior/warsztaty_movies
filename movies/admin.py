from django.contrib import admin
from movies.models import Movie, Person

# Register your models here.

@admin.register(Movie)
class AdminMovie(admin.ModelAdmin):
    list_display = ['title', 'description','director', 'actors','year']
    
@admin.register(Person)
class AdminPerson(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']