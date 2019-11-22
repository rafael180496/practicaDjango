from django.contrib import admin
from  .models import Category,Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # muestre las fechas
    readonly_fields = ('created', 'updated')
    #columnas por mostrar
    list_display = ('title', 'author', 'published','post_categories')
    #campos de ordenar
    ordering = ('author','published')
    #campos de bsuquedas
    #author es un objeto se debe de definir q campo
    search_fields = ('author__username','title','categories__name')
    #busqueda por fecha
    date_hierarchy ='published'
    #filtro
    list_filter = ('author__username','categories__name')

    #categorias
    def post_categories(self,obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    #cambiar nombre
    post_categories.short_description = "Categorias"


class CategoryAdmin(admin.ModelAdmin):
    # muestre las fechas
    readonly_fields = ('created', 'updated')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

