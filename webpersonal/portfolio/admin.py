from django.contrib import admin
from .models import Project #mismo directorio

# Register your models here.
#extender las funcionalidades
class ProjectAdmin(admin.ModelAdmin):
    #muestre las fechas
    readonly_fields = ('created','updated')


admin.site.register(Project,ProjectAdmin)