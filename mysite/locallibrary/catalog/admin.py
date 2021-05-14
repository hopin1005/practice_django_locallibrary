from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

class Authoradmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, Authoradmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #list_display = ('title', 'author', 'display_genre')
    pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre)
#admin.site.register(BookInstance)

