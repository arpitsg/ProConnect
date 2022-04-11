from django.contrib import admin
from .models import Application,Company_profile,Job

# Register your models here.
admin.site.register(Application)
admin.site.register(Company_profile)
admin.site.register(Job)