from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import  render, redirect
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.models import User
from django.contrib.auth import logout

def home_view(request):
    
    return render(request,'main/home.html',{})

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('./')
    
def register_request_company(request):
    if request.user.is_authenticated:
        return redirect('../profiles/myprofile')
    else:
         if request.method == "POST":
            print(request.POST)
            value=request.POST
           
            if User.objects.filter(username=value['userid']).count():
                print('=========repeat')
                messages.error(request, "Username already used")
                return  redirect('./')
            user = User.objects.create(username=value['userid'], email=value['email'])
            user.set_password(value['password1'])
            user.save()
         return render (request, 'proconnect/register_company.html')

def register_request_user(request):
    if request.user.is_authenticated:
         return redirect('../profiles/myprofile')
    else:
        if request.method == "POST":
            value=request.POST
            user = User.objects.create(username=value['userid'], email=value['email'])
            if User.objects.filter(username=value['userid']).count():
                messages.error(request, "Username already used")
                return  redirect('../profiles/myprofile')
            if value['password1']!=value['password2']:
                messages.error(request, "Password not matched")
                return redirect('')

            
            user.set_password(value['password1'])
            user.save()
            

    return render (request, 'proconnect/register_user.html')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name='proconnect/login.html', context={"login_form":form})