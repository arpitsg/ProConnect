from django.shortcuts import render
from company_profile.models import Job,Company_profile
from profiles.models import Profile
from django.db.models import Q
# Create your views here.from django.core.paginator import Paginator
from django.core.paginator import Paginator


def search(request):

    results = []
    page_obj=[]
    if request.method == "POST":

        print(request.POST)
        search=request.POST.get('search')
        option=request.POST.get('option')
        if option=='Job':
           lookup=Q(title__icontains=search)| Q(company__icontains=search)|Q(skills_req__icontains=search)| Q(skills_req__icontains=search)| Q(location__icontains=search)
           qs= Job.objects.filter(lookup)
           print(qs)
           paginator = Paginator(qs, 12)
           page_number = request.GET.get('page')
           page_obj1 = paginator.get_page(page_number)
           context = {

                'page_obj1': page_obj1}
           return render(request, 'searchapp/search.html',context)
        if option=='User':
            lookup=Q(first_name__icontains=search)| Q(last_name__icontains=search)
            qs= Profile.objects.filter(lookup)
            print(qs)
            paginator = Paginator(qs, 12)
            page_number = request.GET.get('page')
            page_obj2 = paginator.get_page(page_number)
            context = {'page_obj2': page_obj2}
            return render(request, 'searchapp/search.html',context)
        if option=='Company':
            lookup=Q(company_name__icontains=search)| Q(location__icontains=search)
            qs= Company_profile.objects.filter(lookup)
            print(qs)
            paginator = Paginator(qs, 12)
            page_number = request.GET.get('page')
            page_obj3 = paginator.get_page(page_number)
            context = {'page_obj3': page_obj3}
            return render(request, 'searchapp/search.html',context)
    return render(request, 'searchapp/search.html')
    

        





    return render(request, 'searchapp/search.html')

    