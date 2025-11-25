from django.contrib import admin
from .models import Libro


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'titulo', 'autor', 'copias_disponibles')
    search_fields = ('isbn', 'titulo', 'autor')
