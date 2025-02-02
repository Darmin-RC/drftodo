from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProyectoViewSet, TareaViewSet, EtiquetaViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)
router.register(r'tareas', TareaViewSet)
router.register(r'etiquetas', EtiquetaViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]