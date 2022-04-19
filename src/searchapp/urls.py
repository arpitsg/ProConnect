from django.urls import path
from .views import search

app_name = 'searchapp'

urlpatterns = [
path('search', search, name='search'),


 ]