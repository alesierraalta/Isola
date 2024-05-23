from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ComidaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'comidas', ComidaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
