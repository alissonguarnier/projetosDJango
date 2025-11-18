from django.db import models

class Filme(models.Model):
   titulo = models.CharField(max_length=255)           # título do livro
   diretor = models.CharField(max_length=255)      # relacionamento com Autor
   ano = models.PositiveIntegerField()                # código ISBN
   genero = models.CharField(max_length=100)             # número de páginas (positivo)
   duracao = models.PositiveIntegerField()                  # ano de publicação (positivo)

   def __str__(self):
       return self.titulo  # representação em string do livro