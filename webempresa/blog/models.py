from django.db import models
from django.utils.timezone  import  now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200,verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    published=models.DateTimeField(verbose_name="Fecha de publicacion",default=now)
    #opcional
    image = models.ImageField(verbose_name="Imagen", upload_to="post",null=True,blank=True)
    #llaves foraneas
    #modelo en cascada
    author=models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE)
    #un post puede tener muchas categorias
    #related_name para busqueda inversa
    categories=models.ManyToManyField(Category,verbose_name="Categorias",related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title