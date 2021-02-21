from django.shortcuts import render
from . models import tracksapp,courses
from django.core.paginator import Paginator
from django.core.mail import send_mail
# Create your views here.

def track_list(request):
    track_list=tracksapp.objects.all()
    paginator = Paginator(track_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'tracks':page_obj}
    return render(request,'tracksapp/track_list.html',context)
    
    

def track_detail(request , slug):
    track_detail = tracksapp.objects.get(slug=slug)
    mycourses = track_detail.courses.all()
    paginator = Paginator(mycourses, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={'track':track_detail,'courses':page_obj,}
    return render(request,'tracksapp/track_detail.html',context)
    

def CourseListView(request,category):
    courses=courses.objects.filter(klasa=category) 
    context={
        'courses':courses,
        'kategori':category
    } 
    return render(request,'tracksapp/track_list.html',context)


class CourseDetailView():
    context_object_name='course'
    template_name='tracksapp/track_detail.html'
    model=courses    