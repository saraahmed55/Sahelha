from django.shortcuts import render
from . models import tracksapp
# Create your views here.

def track_list(request):
    track_list=tracksapp.objects.all()
    print(track_list)
    context={'tracks':track_list}
    return render(request,'tracksapp/track_list.html',context)
    

def track_detail(request , id):
    track_detail = tracksapp.objects.get(id=id)
    context ={'track':track_detail}
    return render(request,'tracksapp/track_detail.html',context)
    