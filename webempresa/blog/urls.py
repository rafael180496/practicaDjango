from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    #core
    path('',views.blog,name="blog"),
    #path con parametro
    path('category/<int:category_id>/',views.category,name="category"),
]