from django.shortcuts import render

# Create your views here.
def web(request):
    
    context ={}
    return render(request,'web/web.html',context)