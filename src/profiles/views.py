from django import forms
from django.shortcuts import render
from .models import Profile
from .forms import ProfileModilfy
# Create your views here.
def my_profile_view(request):
    user_field = Profile.objects.get(user=request.user)
    form=ProfileModilfy(request.POST or None,request.FILES or None,instance=user_field)
    dic ={
        'user_field':user_field,
        'form': form
    }
    return render(request,'profiles/myprofile.html',dic)