from distutils.command.upload import upload
import email
from email.policy import default
import profile
from pydoc import describe
from django.db import connections, models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils import get_random_postfix
# Create your models here.





class Profile(models.Model):
    PROFILE_CHOICE=[
        ('U', 'User'),
        ('C', 'Company')
    ] 
    GENDER=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other'),
        ('S','Prefer not to say')
    ]
    first_name = models.CharField(max_length=200,blank=False)
    last_name = models.CharField(max_length=200,blank=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=1,choices=GENDER,default='S')
    dob=models.DateField(auto_now_add=True)
    
#   account_type  {user,company}
    account_type = models.CharField(max_length=1,choices=PROFILE_CHOICE,default='U')
    about_us=models.CharField(default='No bio....',max_length=1000)
    email = models.EmailField(max_length=200,blank=True)
    picture = models.ImageField(default='avatar.png',upload_to='avatars/')
    connections=models.ManyToManyField(User,related_name='connections',blank=True)

    last_updated_time=models.DateTimeField(auto_now=True)
    created_time=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True, blank=True,max_length=1000)

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
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

class Education (models.Model):
    school = models.CharField(max_length=250,blank=False)
    degree=models.CharField(max_length=250,blank=True)
    field=models.CharField(max_length=250,blank=True)
    start_date = models.DateField(blank=True)
    end_date_expected = models.DateField(blank=True)
    grade=models.CharField(max_length=250,blank=True)
    description = models.CharField(max_length=2500)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

class Experience (models.Model):
    EMPLOYMENT_CHOICE=[
        ('F', 'Full-time'),
        ('P', 'Part-time'),
        ('S', 'Self-employed'),
        ('F', 'Freelance'),
        ('I', 'Internship')
    ] 
    title = models.CharField(max_length=250,blank=False)
    employement_type = models.CharField(max_length=1,choices=EMPLOYMENT_CHOICE)
    company_name=models.CharField(max_length=250,blank=False)
    start_date = models.DateField()
    is_current=models.BooleanField()
    end_date = models.DateField()
    description = models.CharField(max_length=2500)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

class Skills (models.Model):  
    title = models.CharField(max_length=250,blank=False)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

class Languages (models.Model):  
    PROFICIENCY_CHOICE=[
        ('L1','Elementary proficiency0'),
        ('L2','Limited working proficiency'),
        ('L3','Professional working proficiency'),
        ('L4','Full professional proficiency'),
        ('L5','Native or bilingual proficiency'),
    ]
    language_name = models.CharField(max_length=250,blank=False)
    Proficiency=models.CharField(max_length=2,choices=PROFICIENCY_CHOICE)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)



class Address(models.Model):
        street=models.CharField(max_length=255,blank=True)
        city=models.CharField(max_length=255,blank=True)
        profile= models.OneToOneField(Profile,on_delete=models.CASCADE)
        zip=models.IntegerField(blank=True)
        country=models.CharField(max_length=255,blank=True)
        latitude=models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
        longitude=models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)


class Relationship(models.Model):
    STATUS_CHOICE=[
        ('Sent','Sent'),
        ('Accepted','Accepted')
    ]
    sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='receiver')
    status = models.CharField(max_length=8,choices=STATUS_CHOICE)
    last_updated_time=models.DateTimeField(auto_now=True)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.sender}-{self.receiver}-{self.status}"