from django.shortcuts import render

#modelos
from .models import Project


# Create your views here.
def portfolio(request):
    listap= Project.objects.all()
    #contexto
    return render(request,"portfolio/portfolio.html",{'listap':listap})