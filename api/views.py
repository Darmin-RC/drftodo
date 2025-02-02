from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Proyecto, Tarea, Etiqueta, Comentario
from .serializers import ProyectoSerializer, TareaSerializer, EtiquetaSerializer, ComentarioSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticated]  # Proteger el endpoint

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]  # Proteger el endpoint

class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer
    permission_classes = [IsAuthenticated]  # Proteger el endpoint

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated]  # Proteger el endpoint
