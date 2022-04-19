from ast import mod
from datetime import datetime
from distutils.command.upload import upload
import email
from email.policy import default
import profile
from pydoc import describe
from django.db import connections, models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from matplotlib.pyplot import title
from django.core.validators import MinValueValidator, MaxValueValidator
from sqlalchemy import null
from .utils import get_random_postfix
from django.db.models import Q
# Create your models here.

GENDER=[
    ('M', 'Male'),
    ('F', 'Female'),
    ('O','Other'),
    ('S','Prefer not to say')
]
PROFILE_CHOICE=[
    ('U', 'User'),
    ('C', 'Company')
] 
STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class ProfileManager(models.Manager):

    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender=profile) | Q(receiver=profile))
        print(qs)
        print("#########")

        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        print(accepted)
        print("#########")

        available = [profile for profile in profiles if profile not in accepted]
        print(available)
        print("#########")
        return available


    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles
class Profile(models.Model):
    
    
    first_name = models.CharField(max_length=200,blank=False)
    last_name = models.CharField(max_length=200,blank=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=1,choices=GENDER,default='S')
    dob=models.DateField(auto_now_add=True)
    headline=models.CharField(max_length=200,blank=True)
#   account_type  {user,company}
    account_type = models.CharField(max_length=1,choices=PROFILE_CHOICE,default='U')
    about_us=models.CharField(default='No bio....',max_length=1000)
    picture = models.ImageField(default='avatar.png',upload_to='avatars/')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    last_updated_time=models.DateTimeField(auto_now=True)
    created_time=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True, blank=True,max_length=1000)
    objects = ProfileManager()
    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()
    


    def __str__(self) -> str:
        return f"{self.user.username}-{self.created_time}"
    def save(self, *args, **kwargs):
       
        
        set_slug=slugify(str(self.user)+"_"+str(self.first_name) + "_" + str(self.last_name))
        flag=False
        flag=Profile.objects.filter(slug=set_slug).exists()
        while flag == True:
            
            set_slug=slugify(set_slug+"_"+str(get_random_postfix()))
            flag=Profile.objects.filter(slug=set_slug).exists()
        self.slug=set_slug
        super().save( *args, **kwargs)

class Award (models.Model):
    title = models.CharField(max_length=250,blank=False)
    issuer=models.CharField(max_length=250,blank=True)
    issue_date = models.DateField(blank=True)
    description = models.CharField(max_length=2500)
    profileID=models.ForeignKey(User,on_delete=models.CASCADE)

class Education (models.Model):
    school = models.CharField(max_length=250,blank=False)
    degree=models.CharField(max_length=250,blank=True)
    field=models.CharField(max_length=250,blank=True)
    start_date = models.DateField(blank=False,null=True)
    end_date_expected = models.DateField(blank=False,null=True)
    grade=models.CharField(max_length=250,blank=True)
    description = models.CharField(max_length=2500,blank=True)
    profileID=models.ForeignKey(User,on_delete=models.CASCADE)
    

class Experience (models.Model):
    EMPLOYMENT_CHOICE=[
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Self-employed', 'Self-employed'),
        ('Freelance', 'Freelance'),
        ('Internship', 'Internship')
    ] 
    title = models.CharField(max_length=250,blank=False)
    employement_type = models.CharField(max_length=15,choices=EMPLOYMENT_CHOICE,default='Full-time')
    company_name=models.CharField(max_length=250,blank=False)
    start_date = models.DateField(blank=False,null=True)
    end_date =models.DateField(blank=True,null=True)
    description = models.CharField(blank=True,max_length=2500)
    profileID=models.ForeignKey(User,on_delete=models.CASCADE)
    is_current=models.BooleanField(default=True)

class Skills (models.Model):  
    title = models.CharField(max_length=250,blank=False)
    profileID=models.ForeignKey(User,on_delete=models.CASCADE)
    proficiency=models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)],default=0,blank=False)
    def get_str_proficiency(self):
        return 'width: '+str(self.proficiency)+'%'

class Languages (models.Model):  
    PROFICIENCY_CHOICE=[
         ('Elementary-proficiency','Elementary proficiency'),
        ('Limited-working-proficiency','Limited working proficiency'),
        ('Professional-working-proficiency','Professional working proficiency'),
        ('Full-professional-proficiency','Full professional proficiency'),
        ('Native-or-bilingual-proficiency','Native or bilingual proficiency')
    ]
    language_name = models.CharField(max_length=250,blank=False)
    proficiency=models.CharField(max_length=40,choices=PROFICIENCY_CHOICE,default='Elementary-proficiency')
    profileID=models.ForeignKey(User,on_delete=models.CASCADE)
    def proficiency_score(self):
        if self.proficiency=='Elementary-proficiency':
            return 20
        if self.proficiency=='Limited-working-proficiency':
            return 40
        if self.proficiency=='Full-professional-proficiency':
            return 60
        if self.proficiency=='Professional-working-proficiency':
            return 80
        if self.proficiency=='Native-or-bilingual-proficiency':
            return 100
    def get_str_proficiency(self):
        if self.proficiency=='Elementary-proficiency':
            return 'width: 20%'
        if self.proficiency=='Limited-working-proficiency':
            return 'width: 40%'
        if self.proficiency=='Full-professional-proficiency':
            return 'width: 60%'
        if self.proficiency=='Professional-working-proficiency':
            return 'width: 80%'
        if self.proficiency=='Native-or-bilingual-proficiency':
            return 'width: 100%'
        

class Projects (models.Model):  
    STATUS_CHOICE=[
       ('Work-in-Progress','Work in Progress'),
       ('Coming-soon','Coming soon'),
       ('Done','Done')
    ]
    title = models.CharField(max_length=250,blank=False)
    start_date = models.DateField(blank=False,null=True) 
    end_date = models.DateField(blank=True,null=True)
    mentor = models.CharField(blank=True,max_length=250)
    description = models.CharField(blank=True,max_length=250)
    status=models.CharField(max_length=20,choices=STATUS_CHOICE)
    profileID=models.ForeignKey(User,on_delete=models.CASCADE)




class Address(models.Model):
        
        city=models.CharField(max_length=255,blank=True)
        profileID=models.ForeignKey(User,on_delete=models.CASCADE)
        zip=models.IntegerField(blank=True)
        country=models.CharField(max_length=255,blank=True)
        latitude=models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
        longitude=models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)


class RelationshipManager(models.Manager):
    def invitations_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    objects = RelationshipManager()
    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"