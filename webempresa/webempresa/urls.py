"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include #incluir las url
#from core import views as corev
#imagenes
from django.conf import settings



urlpatterns = [
    #core
   # path('',corev.home,name="home"),
   # path('about/',corev.about,name="about"),
   # path('service/',corev.service,name="service"),
   # path('store/',corev.store,name="store"),
   # path('contact/',corev.contact,name="contact"),
   # path('sample/',corev.sample,name="sample"),
   # path('blog/',corev.blog,name="blog"),
    #core
    path('',include('core.urls')),
    #service
    path('service/',include('service.urls')),
    #blog
    path('blog/',include('blog.urls')),
    #page
    path('page/',include('pages.urls')),
    #contact
    path('contact/',include('contact.urls')),
    #admin
    path('admin/', admin.site.urls),
]
#modo de imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
