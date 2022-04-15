from django.urls import path
from .views import my_profile_view,edit_skills,map,other_user

app_name = 'profiles'

urlpatterns = [
 path('myprofile/', my_profile_view, name='my-profile-view'),
 path('myprofile/edit/skills',edit_skills,name='edit-skills'), 
 path('map',map,name='map'),
  path('other_user/<int:id>/',other_user,name='other_user'),
 ]