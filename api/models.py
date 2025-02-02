from django.db import models
from django.contrib.auth.models import User

# Modelo Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    miembros = models.ManyToManyField(User, related_name='proyectos')

    def __str__(self):
        return self.nombre

# Modelo Etiqueta
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Modelo Tarea
class Tarea(models.Model):
    ESTADOS = [
        ('P', 'Pendiente'),
        ('E', 'En Proceso'),
        ('C', 'Completada'),
    ]
    PRIORIDADES = [
        ('B', 'Baja'),
        ('M', 'Media'),
        ('A', 'Alta'),
    ]
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField()
    prioridad = models.CharField(max_length=1, choices=PRIORIDADES, default='M')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tareas')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='tareas')

    def __str__(self):
        return self.titulo

# Modelo Comentario
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.tarea.titulo}"