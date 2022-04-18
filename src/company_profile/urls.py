from django.urls import path
from .views import my_profile_company_view , single_job_view, job_list,saved_job_list,edit_job_view,view_applications,applied_job_list

app_name = 'company_profile'

urlpatterns = [
path('myprofile', my_profile_company_view, name='my_profile_company_view'),
path('single_job/<int:id>/', single_job_view, name="single_job_view"),
path('job_list/', job_list, name='job_list'),
path('saved_job_list/',saved_job_list,name='saved_job_list'),
path('applied_job_list/',applied_job_list,name='applied_job_list'),

path('edit_job_view/<int:id>/',edit_job_view,name='edit_job_view'),
path('view_applications/<int:id>/',view_applications,name='view_applications'),

 ]