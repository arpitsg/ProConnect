import bcrypt
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from waitress import profile
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import  render, redirect
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.hashers import check_password
from profiles.models  import Profile
from company_profile.models import  Company_profile
from django.contrib.auth import authenticate, login


def home_view(request):
    
    return render(request,'main/home.html',{})

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('./')
def CHECK_PASSWORD(password, hash):
    return bcrypt.checkpw(password.encode(), hash.encode())

def MAKE_PASSWORD(password):
    password = password.encode()
    hash = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash.decode()

def register_request_company(request):
    # if request.user.is_authenticated:
    #     return redirect('../profiles/myprofile')
    # else:
         if request.method == "POST":
            print(request.POST)
            value=request.POST
           
            if User.objects.filter(username=value['userid']).count():
                print('=========repeat')
                messages.error(request, "Username already used")
                return  redirect('./')
            user = User.objects.create(username=value['userid'], email=value['email'])
            company=Company_profile.objects.create(user=user)
            company.company_name=value['company_name']
            company.location=value['location']
            company.employee_strength=int(value['employee_strength'])
            company.save()
            user.password=(make_password(value['password1']))
            user.save()
            redirect('../login')
         return render (request, 'proconnect/register_company.html')

def register_request_user(request):
    # if request.user.is_authenticated:
    #      return redirect('../profiles/myprofile')
    # else:
        if request.method == "POST":
            value=request.POST
            print(value)
            
            if User.objects.filter(username=value['userid']).count():
                messages.error(request, "Username already used")
                return  redirect('./')
            if value['password1']!=value['password2']:
                messages.error(request, "Password not matched")
                return redirect('./')
            user = User.objects.create(username=value['userid'], email=value['email'])
            profile=Profile.objects.create(user=user)
            profile.first_name=value['first_name']
            profile.last_name=value['last_name']
            profile.gender=value['gender']
            profile.dob=value['dob']
            profile.save()
            
            user.password=make_password(value['password1'])
            print(user.password)
            user.save()
            return redirect('../login')

            

        return render (request, 'proconnect/register_user.html')

def login_request(request):
    if request.method == "POST":
        print(request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.get(username=username)
        
        print(check_password(password, user.password))
        if check_password(password, user.password): # entered password matches with the password stored in dB
            user = authenticate(username=username, password=password)
            if user is not None:
                print('not none')
                login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            if Profile.objects.filter(user=request.user).count()==0:
                return redirect("company_profile/myprofile")
            else:
                return redirect("profiles/myprofile")

        else:
            print(' not loggedin ')
            messages.error(request,"Invalid username or password.")
       
    form = AuthenticationForm()
    return render(request=request, template_name='proconnect/login.html', context={"login_form":form})