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
from .views import home_view,register_request_user,login_request,logout_view,register_request_company,search_results

# app_name = 'proconnect'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home_view' ),
    path('__debug__/', include('debug_toolbar.urls')),
    path('profiles/',include('profiles.urls',namespace='profiles')),
    path('posts/',include('posts.urls',namespace='posts')),
    path('register_user/', register_request_user, name="register_user"),
    path('register_company/', register_request_company, name="register_company"),
    path('company_profile/',include('company_profile.urls',namespace='company_profile')),
    path('searchapp/',include('searchapp.urls',namespace='searchapp')),
     path("login", login_request, name="login"),
     path('search_results',search_results,name="search_results"),
     path("logout", logout_view, name="logout_view")
    ]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
