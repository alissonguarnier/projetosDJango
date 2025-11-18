from rest_framework import viewsets
from .models import Filme
from .serializers import FilmeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class FilmeViewSet(viewsets.ModelViewSet):
   queryset = Filme.objects.all()
   serializer_class = FilmeSerializer
   permission_classes = [IsAuthenticatedOrReadOnly]
   filter_backends = [DjangoFilterBackend]
   filterset_fields = ['titulo', 'diretor', 'ano', 'genero', 'duracao']
