from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.utils import timezone
from django.template.defaultfilters import slugify

CHOICES = (
    ('Full-Time', 'Full-Time'),
    ('Part-Time', 'Part-Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)

class Company_profile(models.Model):

          user=models.OneToOneField(User,on_delete=models.CASCADE,default='')
          company_name=models.CharField(max_length=255)
          location = models.CharField(max_length=255)
          about_us=models.TextField(default='No bio....',max_length=2000)
          last_updated_time=models.DateTimeField(auto_now=True)
          employee_strength=models.IntegerField(blank=False,default=0)
          
          
          # slug=models.SlugField(unique=True, blank=True,max_length=1000)

          # def save(self, *args, **kwargs):
          #           set_slug=slugify(str(self.user)+"_"+str(self.first_name) + "_" + str(self.last_name))
          #           flag=False
          #           flag=Profile.objects.filter(slug=set_slug).exists()
          #           while flag == True:

          #           set_slug=slugify(set_slug+"_"+str(get_random_postfix()))
          #           flag=Profile.objects.filter(slug=set_slug).exists()
          #           self.slug=set_slug
          #           super().save( *args, **kwargs)

class Job(models.Model):

    company_userID =models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=255,default='-')
    description = models.TextField(blank=False,default='-')
    experience_required=models.CharField(max_length=200,blank=False,default='-')
    salary=models.IntegerField(blank=True,default=-1)
    skills_req = models.CharField(max_length=200)
    job_type = models.CharField(
        max_length=30, choices=CHOICES, default='Full Time', null=True)
    link = models.URLField(null=True, blank=True)
#     slug = AutoSlugField(populate_from='title', unique=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    deadline =models.DateTimeField(blank=False,null=True)

    def __str__(self):
        return self.title

class SavedJob(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_time=models.DateTimeField(auto_now_add=True,null=True )
    def __str__(self):
        return self.job.title

# class Applicants(models.Model):
#     job = models.ForeignKey(
#         Job, related_name='applicants', on_delete=models.CASCADE)
#     applicant = models.ForeignKey(
#         User, related_name='applied', on_delete=models.CASCADE)
#     date_posted = models.DateTimeField(default=timezone.now)
#     date_applied=models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.applicant

class Application(models.Model):


    APPLICATION_CHOICES = (
        ('Active', 'ACTIVE'),
        ('Selected', 'SELECTED'),
        ('Rejected', 'REJECTED'),
        {'Interview', 'INTERVIEW'},
    )


    seeker = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15,
                              choices=APPLICATION_CHOICES,
                              default='Active')
    comment=models.TextField(blank=True,max_length=250)