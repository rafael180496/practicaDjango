from django.db import models

# Create your models here.

class Service(models.Model):
    title=models.CharField(verbose_name="Titulo",max_length=200)
    subtitle=models.CharField(verbose_name="Subtitulo",max_length=200)
    content=models.TextField(verbose_name="Contenido")
    image=models.ImageField(verbose_name="Imagen",upload_to="service")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural="Servicios"
        ordering=['-created']

    def __str__(self):
        return self.title