#ruteo de core

from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    #core
    path('',views.service,name="service"),

]