from django.shortcuts import render
from .models import Service

# Create your views here.
def service(request):
    listS=Service.objects.all()
    return render(request,"service/services.html",{'serv':listS})