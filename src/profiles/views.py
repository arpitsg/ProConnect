from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Profile , Skills  ,Address,Award,Education,Experience,Projects,Languages
from .forms import ProfileModilfy ,SkillModilfy
from django.contrib.auth.models import User
# Create your views here.
def check_if_starts(dic,word):
    
    return  {key:val for key, val in dic.items() 
                   if key.startswith(word)}

def edit_skills(request):
    try:
        skills=list(Skills.objects.filter(profileID=request.user))
    except Skills.DoesNotExist:
         skills=None
    
    if skills==None:
        return HttpResponseRedirect("profiles/myprofile")
    forms_skill=[]
    for i in skills:
        print((i.title))
        forms_skill.append(SkillModilfy(request.POST or None,request.FILES or None,instance=i))
    
    if request.method == 'POST':
        
        skill=Skills.objects.filter(id=request.POST.get('id'))[0]
        print(skill)
        print(vars(skill))
        
        
    
    dic={ 
            'skills':skills,
                'forms_skill':forms_skill,
                'skill_zip':zip(forms_skill,skills)
            }
    return  render(request,'profiles/skill_edit_form.html',dic)
    

def my_profile_view(request):
    # print("Userid->",request.user)
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    try:
        address=list(Address.objects.filter(profileID=request.user))
    except Address.DoesNotExist:
        address=None
    try:
        skills=list(Skills.objects.filter(profileID=request.user))
    except Skills.DoesNotExist:
        skills=None
    try:
        education=list(Education.objects.filter(profileID=request.user).order_by('start_date'))
    except Education.DoesNotExist:
        education=None
    try:
        awards=list(Award.objects.filter(profileID=request.user))
    except Award.DoesNotExist:
        awards=None
    try:
        experience=list(Experience.objects.filter(profileID=request.user).order_by('start_date'))
    except Experience.DoesNotExist:
        experience=None
    try:
        projects=list(Projects.objects.filter(profileID=request.user).order_by('start_date'))
    except Experience.DoesNotExist:
        projects=None
    try:
        skills=list(Skills.objects.filter(profileID=request.user).order_by('proficiency'))
    except Experience.DoesNotExist:
        skills=None
    try:
        languages=list(Languages.objects.filter(profileID=request.user))
    except Experience.DoesNotExist:
        languages=None
    
    # str=[key for key in check_if_starts(request.POST,'skill_submit').keys()]
    

    # i=int(str.split('_')[-1])
    # form_skill=SkillModilfy(request.POST or None,request.FILES or None,instance=skills[i])

    if request.method == 'POST':
     print("request.POST->here",request.POST)
    # if not not check_if_starts(request.POST,'skill_submit_button'):
    #     str=[key for key in check_if_starts(request.POST,'skill_submit').keys()][0]
    #     i=int(str.split('_')[-1])
    #     form=SkillModilfy(request.POST or None,request.FILES or None,instance=skills[i])
    #     if request.method == 'POST':
    #         if form.is_valid():
    #             form.save()

    form_profile=ProfileModilfy(request.POST or None,request.FILES or None,instance=profile)
    if request.method == 'POST':
        if form_profile.is_valid():
            form_profile.save()

    form_language=[]
    
    form_skill=[]
    for i in skills:
        form_skill.append(SkillModilfy(request.POST or None,request.FILES or None,instance=i))
    form_education=[]
    form_project=[]






    dic ={
        'profile':profile,
        'form_profile': form_profile,
        'form_skill':form_skill[0],
        'user':request.user,
        'address':address,
        'education_check':(education==None),
        'skills':skills,
        'education':education,
        'awards':awards,
        'experience':experience,
        'projects':projects,
        'languages':languages
    }
    return render(request,'profiles/myprofile.html',dic)