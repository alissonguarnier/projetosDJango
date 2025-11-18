from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from filmes.views import FilmeViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'filmes', FilmeViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),           # rota do Django admin
   path('api/', include(router.urls)),        # inclui rotas geradas pelo router sob o prefixo /api/
   path('api/token/', obtain_auth_token),      # POST com username e password

]
