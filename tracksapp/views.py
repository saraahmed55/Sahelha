from django.shortcuts import render
from . models import tracksapp
from django.core.paginator import Paginator
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
    context ={'track':track_detail}
    return render(request,'tracksapp/track_detail.html',context)
    