"""
URL configuration for aluga_car project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from app.views import CarroViewSet, LocacaoViewSet

# O Router lê as ViewSets e cria todas as rotas padrão da API automaticamente
router = routers.DefaultRouter()

# Rota para os carros:
# Cria endpoints: /api/carros/ e /api/carros/<id>/
# 'basename' ajuda a nomear as rotas internas geradas pelo DRF
router.register(r'carros', CarroViewSet, basename='carro')

# Rota para as locações:
# Cria endpoints: /api/locacoes/ e /api/locacoes/<id>/
router.register(r'locacoes', LocacaoViewSet, basename='locacao')

urlpatterns = [
    path("admin/", admin.site.urls),
    # include(router.urls) injeta todas as rotas geradas pelo router na URL base do app
    path('', include(router.urls)),
]
