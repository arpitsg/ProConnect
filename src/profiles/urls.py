from django.urls import path
from .views import get_friends_list, my_profile_view,edit_skills,other_user,add_education,add_experience,add_skill,add_language,add_project,edit_language,edit_skill,edit_education,edit_project,edit_experience,delete_language,delete_skill,delete_education,delete_experience,delete_project,invites_received_view, profiles_list_view,invite_profiles_list_view, ProfileDetailView,ProfileListView,send_invitation,remove_from_friends,accept_invitation,reject_invitation,get_friends_list
app_name = 'profiles'

urlpatterns = [
 path('myprofile/', my_profile_view, name='my-profile-view'),
 path('add_education', add_education, name='add_education'),
 path('add_experience', add_experience, name='add_experience'),
 path('add_skill', add_skill, name='add_skill'),
path('add_language', add_language, name='add_language'),
path('add_project', add_project, name='add_project'),

path('edit_language/<int:id>/', edit_language, name='edit_language'),

path('edit_skill/<int:id>/', edit_skill, name='edit_skill'),
path('edit_project/<int:id>/', edit_project, name='edit_project'),
path('edit_education/<int:id>/', edit_education, name='edit_education'),
path('edit_experience/<int:id>/', edit_experience, name='edit_experience'),
path('edit_project/<int:id>/', edit_project, name='edit_project'),

path('delete_language/<int:id>/', delete_language, name='delete_language'),
path('delete_skill/<int:id>/', delete_skill, name='delete_skill'),
path('delete_education/<int:id>/', delete_education, name='delete_education'),
path('delete_experience/<int:id>/', delete_experience, name='delete_experience'),
path('delete_project/<int:id>/', delete_project, name='delete_project'),

 path('myprofile/edit/skills',edit_skills,name='edit-skills'), 
 path('map',map,name='map'),
  path('other_user/<int:id>/',other_user,name='other_user'),
  path('', ProfileListView.as_view(), name='all-profiles-view'),
  path('my-invites/', invites_received_view, name='my-invites-view'),
  path('friends_list/', get_friends_list, name='friends_list_view'),
  path('send-invite/', send_invitation, name='send-invite'),
  path('remove-friend/', remove_from_friends, name='remove-friend'),
  path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
  path('my-invites/accept/', accept_invitation, name='accept-invite'),
  path('my-invites/reject/', reject_invitation, name='reject-invite'),
 ]