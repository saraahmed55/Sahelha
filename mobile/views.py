from django.shortcuts import render

# Create your views here.
def mobile(request):

    context ={}
    return render(request,'mobile/mobile.html',context)