from django.shortcuts import render

# Create your views here.
def machine(request):
    
    context ={}
    return render(request,'machine/machine.html',context)