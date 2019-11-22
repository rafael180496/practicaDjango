from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200,verbose_name="Titulo")
    description=models.TextField(verbose_name="Descripcion")
    image=models.ImageField(verbose_name="Imagen",upload_to='projects')
    created=models.DateTimeField(auto_now_add=True,verbose_name="Crecion")
    updated=models.DateTimeField(auto_now=True,verbose_name="Edicion")
    #para que sea oopcional
    link =models.URLField(null=True,blank=True,verbose_name="Link de proyecto")

    class Meta:
        #meta datos para el modelo
        #nombre
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
        ordering=["-created"]

    #para que salga el administrador mejor
    def __str__(self):
        return self.title
