from django.contrib import admin
from .models import Application,Company_profile,Job
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
# Register your models here.
admin.site.register(Application)
admin.site.register(Company_profile)
admin.site.register(Job)

class ExtendUser(models.Model):
    r = models.OneToOneField(User,on_delete=models.CASCADE)
    is_company=models.BooleanField(default=True,blank=False)
    is_user=models.CharField(default='a',max_length=255)
    def __str__(self):
        return self.r.username