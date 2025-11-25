from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, prestamos_semana, prestamos_multa

router = DefaultRouter()
router.register(r'libros', LibroViewSet, basename='libro')

urlpatterns = [
    path('', include(router.urls)),
    path('prestamos/semana', prestamos_semana, name='prestamos-semana'),
    path('prestamos/multa', prestamos_multa, name='prestamos-multa'),
]
