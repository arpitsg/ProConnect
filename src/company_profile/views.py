from calendar import c
from email.mime import application
import re
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import Job_form,Update_profile,Application_Update
# Create your views here.
from .models import Job,Company_profile,Application,SavedJob

def check_if_starts(dic,word):
    
    return  {key:val for key, val in dic.items() 
                   if key.startswith(word)}

def view_applications(request,id):
     job=get_object_or_404(Job,id=id)
     if job.id!=id:
         return HttpResponseNotFound('<h1>Invalid access </h1>')
     applications=Application.objects.filter(job=job)
     if request.method=='POST':
         print(request.POST)
    
     forms=[Application_Update(instance=i) for i in applications]
     context={'applications':applications,
                        'forms':forms,
                        'zipped': zip(applications,forms)
                        }
     return render(request,'company_profile/view_applications.html',context)

def my_profile_company_view(request):

    

    company=get_object_or_404(Company_profile,user=request.user)
    total_jobs = Job.objects.filter(company_userID=request.user).count()
    
    job_form=Job_form()
    profile_form=Update_profile(instance=company)
    my_jobs=Job.objects.filter(company_userID=request.user)
    paginator = Paginator(my_jobs, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method =='POST':
        
        re=request.POST
        print(re)
        if not not check_if_starts(re,'add_job'):
    
            current_job=Job.objects.create(company_userID=request.user  )
            current_job.title= re.get('title')
            current_job.description= re.get('description')
            current_job.experience_required= re.get('experience_required')
            current_job.skills_req= re.get('skills_req')
            current_job.job_type= re.get('job_type')
            current_job.deadline= re.get('deadline')
            current_job.company=company.company_name
            current_job.location=re.get('location')
            current_job.save()
            return redirect('/company_profile/myprofile')
        if not not check_if_starts(re,'profile_update'):
            profile_form=Update_profile(re,instance=company)
            if profile_form.is_valid():
                profile_form.save()
            return redirect('/company_profile/myprofile')
                

          
    context={
                    'profile_form':profile_form,
                    'my_jobs':my_jobs,
                    'page_obj':page_obj,
                    'job_form':job_form,
                    'company':company,
                    'total_jobs':total_jobs,}
    return render(request, 'company_profile/myprofile.html',context)

# @login_required(login_url=reverse_lazy('proconnect:login'))
def saved_job_list(request):

    saved_list = SavedJob.objects.filter(user=request.user)
    job_list=[s.job for s in saved_list]
    paginator = Paginator(job_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {

        'page_obj': page_obj,

    }
    return render(request, 'company_profile/saved_job_list.html', context)

def job_list(request):

    job_list = Job.objects.order_by('-date_posted')
    paginator = Paginator(job_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {

        'page_obj': page_obj,

    }
    return render(request, 'company_profile/job_list.html', context)



def single_job_view(request,id):
    print(request.user)
    print("id->",id)
    
    company=Company_profile.objects.filter(user=request.user)
    print(company.count())
    role='user'
    if company.count()==0:
        role='user'
    else :
        role='company'
    job_query = get_object_or_404(Job, id=id)
    saved=0
    if SavedJob.objects.filter(user=request.user,job=job_query).count()>0:
        saved=1
    applied=0
    if Application.objects.filter(seeker=request.user,job=job_query).count()>0:
        applied=1
   
    
            


    print(vars(job_query))
    context = {
        'job': job_query,
        'user': request.user,
        'role': role,
        'saved':saved,
        'applied':applied,
    }
    if request.method == 'POST':
        re= request.POST
        print(check_if_starts(re,'apply'))
        print(check_if_starts(re,'withdraw'))
        print(check_if_starts(re,'save'))
        print(check_if_starts(re,'unsave'))

        if not not check_if_starts(re,'apply'):
            print('apppling')
            Application.objects.create(seeker=request.user,job=job_query)
            return redirect('/company_profile/single_job/'+str(id))
        if  not not check_if_starts(re,'withdraw'):
            Application.objects.filter(seeker=request.user,job=job_query).delete()
            return redirect('/company_profile/single_job/'+str(id))
        if not not check_if_starts(re,'save'):
            print('saving')
            SavedJob.objects.create(user=request.user,job=job_query)
            return redirect('/company_profile/single_job/'+str(id))
        if not not check_if_starts(re,'unsave'):
            SavedJob.objects.filter(user=request.user,job=job_query).delete()
            return redirect('/company_profile/single_job/'+str(id))

            

    return render(request, 'company_profile/single_job.html', context)





def edit_job_view(request,id):
    if request.user!=Job.objects.get(id=id).company_userID:
        return HttpResponseNotFound('<h1>Invalid access </h1>')



    if request.method == 'POST':
        joob=Job.objects.get(id=id)
        if not not check_if_starts(request.POST,'add_job'):
            job_form=Job_form(request.POST,instance=joob)
            if job_form.is_valid():
                job_form.save()
            return redirect('/company_profile/myprofile')
        if not not check_if_starts(request.POST,'delete_job'):
            joob.delete()
            print('deleted')
            return redirect('/company_profile/myprofile')
    if Job.objects.filter(id=id).count()==0:
        return redirect('/company_profile/myprofile')
    else:
        job_form=Job_form(instance=Job.objects.get(id=id))
        context={'job_form':job_form}
        return render(request, 'company_profile/job_edit.html',context)
