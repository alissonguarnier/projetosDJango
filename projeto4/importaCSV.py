import csv
from filmes.models import Filme

# Caminho para o CSV
CAMINHO_CSV = 'base_filmes.csv'

with open(CAMINHO_CSV, newline='', encoding='utf-8') as csvfile:
   arquivo = csv.DictReader(csvfile)
   for linha in arquivo:
      Filme.objects.create(
            titulo=linha['titulo'],
            diretor=linha['diretor'],
            ano=linha['ano'],
            genero=linha['genero'],
            duracao=linha['duracao']
      )
print("Importação concluída com sucesso!")