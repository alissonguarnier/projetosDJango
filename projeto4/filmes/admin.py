from django.contrib import admin
from .models import Filme
from rest_framework.authtoken.models import Token


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
  list_display = ['titulo', 'diretor', 'ano', 'genero', 'duracao']   
  search_fields = ['titulo', 'diretor', 'ano', 'genero', 'duracao']
  list_filter = ['titulo', 'diretor', 'ano', 'genero', 'duracao']


admin.site.register(Token)