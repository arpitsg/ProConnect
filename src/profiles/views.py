from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from requests import request
from .models import Profile , Skills  ,Address,Award,Education,Experience,Projects,Languages
from .forms import ProfileModilfy ,SkillModilfy,LangModilfy,ExperienceModify,EducationModify,ProjectModify
from django.contrib.auth.models import User
import datetime
import folium
import geocoder
from .utils import get_ip_address,get_geo

def other_user(request,id):
    print('no found',id)
    user=get_object_or_404(User,id=id)
    print('user_found')
    profile = get_object_or_404(Profile,user=user)
    print('profiler_found')
    try:
        educations=list(Education.objects.filter(profileID=user).order_by('start_date'))
    except Education.DoesNotExist:
        educations=None
    try:
        awards=list(Award.objects.filter(profileID=user))
    except Award.DoesNotExist:
        awards=None
    try:
        experiences=list(Experience.objects.filter(profileID=user).order_by('start_date'))
    except Experience.DoesNotExist:
        experiences=None
    try:
        projects=list(Projects.objects.filter(profileID=user).order_by('start_date'))
    except Experience.DoesNotExist:
        projects=None
    try:
        skills=list(Skills.objects.filter(profileID=user).order_by('proficiency'))
    except Experience.DoesNotExist:
        skills=None
    try:
        languages=list(Languages.objects.filter(profileID=user))
    except Experience.DoesNotExist:
        languages=None

    dic={'skills':skills,
        'educations':educations,
        'awards':awards,
        'experiences':experiences,
        'projects':projects,
        'languages':languages
    }
    return render(request,'profiles/other_user.html',dic)

def map(request):
    
    
    # Create Map Object
    map = folium.Map(location=[19, -12], zoom_start=2)
    ip=get_ip_address(request)
    country, city, lat, lon=get_geo(ip)
    folium.Marker([lat, lon], tooltip='Click for more',
                  popup=country).add_to(map)
    # Get HTML Representation of Map Object
    map = map._repr_html_()
    context = {
        'map': map,
    }
    return render(request, 'profiles/map.html', context)

def check_if_starts(dic,word):
    
    return  {key:val for key, val in dic.items() 
                   if key.startswith(word)}

def edit_skills(request):
    try:
        skills=list(Skills.objects.all().filter(profileID=request.user))
    except Skills.DoesNotExist:
         skills=None
    
    if skills==None:
        return HttpResponseRedirect("profiles/myprofile")
    forms_skill=[]
    for i in skills:
        print(len(forms_skill))
        print((i.title))
        print("------------------printing form----------")
        fo=SkillModilfy(request.POST,instance=i)
        print(fo)
        forms_skill.append(fo)
        print("in for loop",forms_skill)
    # for x in forms_skill:
    #     print("------------------printing form----------")
    #     print(x)

    # if request.method == 'POST':
        
    #     skill=Skills.objects.filter(id=request.POST.get('id'))[0]
    #     idx=0
    #     while skill != skills[idx]:
    #         idx+=1
    #     print(skill)
    #     print(vars(skill))
    #     post=request.POST
        
    #     skill.title=post.getlist('title')[idx]
    #     skill.proficiency=int(post.getlist('proficiency')[idx])
    #     skill.save()
        

        
        
    
    dic={ 
            'skills':skills,
                'forms_skill':forms_skill,
                'skill_zip':zip(forms_skill,skills)
            }
    return  render(request,'profiles/skill_edit_form.html',dic)
    

def my_profile_view(request):
    # print("Userid->",request.user)
    profile = get_object_or_404(Profile,user=request.user)
    try:
        address=list(Address.objects.filter(profileID=request.user))
    except Address.DoesNotExist:
        address=None
    try:
        skills=list(Skills.objects.filter(profileID=request.user))
    except Skills.DoesNotExist:
        skills=None
    try:
        educations=list(Education.objects.filter(profileID=request.user).order_by('start_date'))
    except Education.DoesNotExist:
        educations=None
    try:
        awards=list(Award.objects.filter(profileID=request.user))
    except Award.DoesNotExist:
        awards=None
    try:
        experiences=list(Experience.objects.filter(profileID=request.user).order_by('start_date'))
    except Experience.DoesNotExist:
        experiences=None
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

    # if request.method == 'POST':
    #     print("f---------")
    #     print("request.POST->here",request.POST)
    #     for i in skills:
    #         print(i.proficiency)
   

    form_profile=ProfileModilfy(request.POST or None,request.FILES or None,instance=profile)
    
    project_form=[ProjectModify(instance=i) for i in projects]
    skill_form=[SkillModilfy(instance=i) for i in skills]
    education_form=[EducationModify(instance=i) for i in educations]
    experience_form=[ExperienceModify(instance=i) for i in experiences]
    language_form=[LangModilfy(instance=i) for i in languages]

    # experience_form=ExperienceModify(request.POST,instance=experiences[0])
    
    # for i in languages:
    #     languages_form.append(LangModilfy(request.POST,instance=i))
    #     print(LangModilfy(request.POST,instance=i))
   

    import re
    def change_date_format(dt):
            return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)



    if request.method == 'POST':
        print(request.POST)
        if not not check_if_starts(request.POST ,'profile_submit'):
            if form_profile.is_valid():
                form_profile.save()
        if not not check_if_starts(request.POST ,'skill_modilfy_submit'):
            title = request.POST.getlist("title")
            proficiency_skill=request.POST.getlist("proficiency")
            for i in range(len(skills)):
                skills[i].title=title[i]
                skills[i].proficiency=proficiency_skill[i]
                skills[i].save()
        if not not check_if_starts(request.POST,'language_modilfy_submit'):
            language_name = request.POST.getlist("language_name")
            proficiency_lang=request.POST.getlist("proficiency")
            for i in range(len(languages)):
                languages[i].language_name=language_name[i]
                languages[i].proficiency=proficiency_lang[i]
                languages[i].save()
        if not not check_if_starts(request.POST,'experience_modilfy_submit'):
            print('here experience_modilfy_submit')
            title=request.POST.getlist('title')
            employement_type=request.POST.getlist('employement_type')
            company_name=request.POST.getlist('company_name')
            start_date=request.POST.getlist('start_date')
            end_date=request.POST.getlist('end_date')
            description=request.POST.getlist('description')
            for i in range(len(experiences)):
                experiences[i].title=title[i]
                experiences[i].employement_type=employement_type[i]
                experiences[i].company_name=company_name[i]
                experiences[i].start_date=start_date[i]
              
                experiences[i].end_date=end_date[i]
                if experiences[i].end_date=='':
                    experiences[i].end_date=None
                
            
                experiences[i].description=description[i]
                             
                experiences[i].save()



        if not not check_if_starts(request.POST,'education_modilfy_submit'):
            school=request.POST.getlist('school')
            degree=request.POST.getlist('degree')
            field=request.POST.getlist('field')
            start_date=request.POST.getlist('start_date')
            end_date_expected=request.POST.getlist('end_date_expected')
            grade=request.POST.getlist('grade')
            description=request.POST.getlist('description')

            for i in range(len(educations)):
                educations[i].school=school[i]
                educations[i].degree=degree[i]
                educations[i].field=field[i]
                educations[i].start_date=start_date[i]
                educations[i].end_date_expected=end_date_expected[i]
                educations[i].grade=grade[i]
                educations[i].description=description[i]    
                educations[i].save()



        if not not check_if_starts(request.POST,'project_modilfy_submit'):
            print("hereeeeee")
            title=request.POST.getlist('title')
            start_date=request.POST.getlist('start_date')
            end_date=request.POST.getlist('end_date')
            mentor=request.POST.getlist('mentor')
            description=request.POST.getlist('description')
            status=request.POST.getlist('status')
            for i in range(len(projects)):
                projects[i].title=title[i]
                projects[i].start_date=start_date[i]
                projects[i].end_date=end_date[i]
                if projects[i].end_date=='':
                    projects[i].end_date=None
                projects[i].mentor=mentor[i]
                projects[i].description=description[i]
                projects[i].status=status[i]    
                projects[i].save()
                print("saved")

        
        
    


        

    

              

    dic ={
        'language_form':language_form,
        'skill_form':skill_form,
        'experience_form':experience_form,
        'education_form':education_form,
        'project_form':project_form,
        'profile':profile,
        'form_profile': form_profile,
        'skills':skills,
        'user':request.user,
        'address':address,
        
        'skills':skills,
        'educations':educations,
        'awards':awards,
        'experiences':experiences,
        'projects':projects,
        'languages':languages
    }
    return render(request,'profiles/myprofile.html',dic)