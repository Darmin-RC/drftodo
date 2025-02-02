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

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticated]  # Proteger el endpoint
    def get_queryset(self):
        return Proyecto.objects.filter(miembros=self.request.user)

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]  # Proteger el endpoint
    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer
    permission_classes = [IsAuthenticated]  # Proteger el endpoint

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated]  # Proteger el endpoint
    def get_queryset(self):
        return Comentario.objects.filter(usuario=self.request.user)
