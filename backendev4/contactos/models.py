from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)#campos de formualrio crear contacto

    def __str__(self):
        return self.nombre

class Visita(models.Model):#conteo de visitas de  la pagina
    conteo = models.IntegerField(default=0)

    def __str__(self):
        return str(self.conteo)