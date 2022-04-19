from django import forms
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from requests import request
from .models import Profile , Skills  ,Address,Award,Education,Experience,Projects,Languages,Relationship
from .forms import ProfileModilfy ,SkillModilfy,LangModilfy,ExperienceModify,EducationModify,ProjectModify
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
import datetime
import folium
import geocoder
from django.db.models import Q
from .utils import get_ip_address,get_geo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
def add_education(request):
    form=EducationModify()
    print('here')
    if request.method=='POST':
        print(request.POST)
        edu=Education.objects.create(profileID=request.user)
        form=EducationModify(request.POST,instance=edu)
        if form.is_valid():
            form.save()
        return redirect('/profiles/myprofile/')
    dic={'form':form}
    return render(request,'profiles/form.html',dic)

def add_experience(request):
    form=ExperienceModify()
    if request.method=='POST':
        print(request.POST)
        exp=Experience.objects.create(profileID=request.user)
        form=ExperienceModify(request.POST,instance=exp)
        if form.is_valid():
            form.save()
        return redirect('/profiles/myprofile/')
    dic={'form':form}
    return render(request,'profiles/form.html',dic)


def add_project(request):
    form=ProjectModify()
    if request.method=='POST':
        print(request.POST)
        exp=Projects.objects.create(profileID=request.user)
        form=ProjectModify(request.POST,instance=exp)
        if form.is_valid():
            form.save()
        return redirect('/profiles/myprofile/')
    dic={'form':form}
    return render(request,'profiles/form.html',dic)
def add_language(request):
    form=LangModilfy()
    if request.method=='POST':
        print(request.POST)
        exp=Languages.objects.create(profileID=request.user)
        form=LangModilfy(request.POST,instance=exp)
        if form.is_valid():
            form.save()
        return redirect('/profiles/myprofile/')
    dic={'form':form}
    return render(request,'profiles/form.html',dic)

def add_skill(request):
    form=SkillModilfy()
    if request.method=='POST':
        print(request.POST)
        exp=Skills.objects.create(profileID=request.user)
        form=SkillModilfy(request.POST,instance=exp)
        if form.is_valid():
            form.save()
        return redirect('/profiles/myprofile/')
    dic={'form':form}
    return render(request,'profiles/form.html',dic)
def edit_language(request,id):
    lang=Languages.objects.get(id=id)
    form=LangModilfy(instance=lang)
    if request.method=='POST':
        print(request.POST)
        
        if(lang.profileID!=request.user):
            return HttpResponseNotFound('<h1>Invalid access </h1>')
        form=LangModilfy(request.POST,instance=lang)
        if form.is_valid():
            form.save()
        return redirect('/profiles/myprofile/')
    dic={'form':form}
    return render(request,'profiles/form.html',dic)

def edit_skill(request,id):
    lang=Skills.objects.get(id=id)
    form=SkillModilfy(instance=lang)
    if request.method=='POST':
        print(request.POST)
        
        if(lang.profileID!=request.user):
            return HttpResponseNotFound('<h1>Invalid access </h1>')
        form=SkillModilfy(request.POST,instance=lang)
        if form.is_valid():
            form.save()
        return redirect('/profiles/myprofile/')
    dic={'form':form}
    return render(request,'profiles/form.html',dic)

def edit_education(request,id):
    lang=Education.objects.get(id=id)
    form=EducationModify(instance=lang)
    if request.method=='POST':
        print(request.POST)
        
        if(lang.profileID!=request.user):
            return HttpResponseNotFound('<h1>Invalid access </h1>')
        form=EducationModify(request.POST,instance=lang)
        if form.is_valid():
            form.save()
        return redirect('/profiles/myprofile/')
    dic={'form':form}
    return render(request,'profiles/form.html',dic)

def edit_project(request,id):
    lang=Projects.objects.get(id=id)
    form=ProjectModify(instance=lang)
    if request.method=='POST':
        print(request.POST)
      
        if(lang.profileID!=request.user):
            return HttpResponseNotFound('<h1>Invalid access </h1>')
        form=ProjectModify(request.POST,instance=lang)
        if form.is_valid():
            form.save()
        return redirect('/profiles/myprofile/')
    dic={'form':form}
    return render(request,'profiles/form.html',dic)
def edit_experience(request,id):
    lang=Experience.objects.get(id=id)
    form=ExperienceModify(instance=lang)
    if request.method=='POST':
        print(request.POST)
        
        if(lang.profileID!=request.user):
            return HttpResponseNotFound('<h1>Invalid access </h1>')
        form=ExperienceModify(request.POST,instance=lang)
        if form.is_valid():
            form.save()
        return redirect('/profiles/myprofile/')
    dic={'form':form}
    return render(request,'profiles/form.html',dic)

def delete_skill(request,id):
    Skills.objects.get(id=id).delete()
    return redirect('/profiles/myprofile/')
def delete_language(request,id):
    Languages.objects.get(id=id).delete()
    return redirect('/profiles/myprofile/')
def delete_education(request,id):
    Education.objects.get(id=id).delete()
    return redirect('/profiles/myprofile/')
def delete_experience(request,id):
    Experience.objects.get(id=id).delete()
    return redirect('/profiles/myprofile/')
def delete_project(request,id):
    Projects.objects.get(id=id).delete()
    return redirect('/profiles/myprofile/')

    
    
def other_user(request,id):
    print('no found',id)
    user=get_object_or_404(User,id=id)
    print('user_found')
    print(user)
    profile = get_object_or_404(Profile,user=user)
    print('profiler_found')
    rel_r = Relationship.objects.filter(sender=profile)
    rel_s = Relationship.objects.filter(receiver=profile)
    rel_receiver = []
    rel_sender = []
    for item in rel_r:
        rel_receiver.append(item.receiver.user)
    for item in rel_s:
        rel_sender.append(item.sender.user)
    print(rel_sender)
    print(rel_receiver)
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
    
    dic={
        'user':user,
        'profile':profile,
        'skills':skills,
        'educations':educations,
        'awards':awards,
        'experiences':experiences,
        'projects':projects,
        'languages':languages,
        'rel_receiver': rel_receiver,
        'rel_sender': rel_sender
    }

    return render(request,'profiles/other_user.html',dic)

def map_view(request):
    
    
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


@login_required
def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invitations_received(profile)
    results = list(map(lambda x: x.sender, qs))
    is_empty = False
    if len(results) == 0:
        is_empty = True

    context = {
        'qs': results,
        'is_empty': is_empty,
    }

    return render(request, 'profiles/my_invites.html', context)

@login_required
def accept_invitation(request):
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        if rel.status == 'send':
            rel.status = 'accepted'
            rel.save()
    return redirect('profiles:my-invites-view')

@login_required
def reject_invitation(request):
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        receiver = Profile.objects.get(user=request.user)
        sender = Profile.objects.get(pk=pk)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        rel.delete()
    return redirect('profiles:my-invites-view')

@login_required
def invite_profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invite(user)
    print(qs)
    context = {'qs': qs}

    return render(request, 'profiles/to_invite_list.html', context)
@login_required
def get_friends_list(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)
    context = {'qs': qs}
    print(qs)
    return render(request, 'profiles/friends_list.html', context)

@login_required
def profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)

    context = {'qs': qs}

    return render(request, 'profiles/profile_list.html', context)

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/detail.html'

    # def get_object(self):
    #     slug = self.kwargs.get('slug')
    #     profile = Profile.objects.get(slug=slug)
    #     return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        context['posts'] = self.get_object().get_all_authors_posts()
        context['len_posts'] = True if len(self.get_object().get_all_authors_posts()) > 0 else False
        return context

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    # context_object_name = 'qs'

    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        context['is_empty'] = False
        if len(self.get_queryset()) == 0:
            context['is_empty'] = True

        return context

@login_required
def send_invitation(request):
    if request.method=='POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        Relationship.objects.create(sender=sender, receiver=receiver, status='send')

        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:my-profile-view')
    
@login_required
def remove_from_friends(request):
    if request.method=='POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.get(
            (Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender))
        )
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:my-profile-view')