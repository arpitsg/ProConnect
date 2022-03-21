"""proconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from turtle import home
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import include, path
from  django.conf import settings
from  django.conf.urls.static import static
from django.views.static import serve 
import  debug_toolbar
from .views import home_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home-view' ),
    path('__debug__/', include('debug_toolbar.urls')),
    path('profiles/',include('profiles.urls',namespace='profiles'))
    ]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
