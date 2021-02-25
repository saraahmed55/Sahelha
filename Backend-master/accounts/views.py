
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.paginator import Paginator
from django.shortcuts import redirect,render
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings
from .models import Profile
from django.urls import reverse
from django.http import HttpResponseRedirect
from tracksapp.models import courses
# Create your views here.
@ login_required
def favourite_list(request):
    profile = Profile.objects.get(user=request.user)
    new = courses.newmanager.filter(favourites=request.user)
    paginator = Paginator(new, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'accounts/favourites.html',{'profile':profile, 'new':page_obj})



@ login_required
def favourite_add(request, id):
    course=get_object_or_404(courses,id=id)
    if course.favourites.filter(id=request.user.id).exists():
        course.favourites.remove(request.user)
    else:
        course.favourites.add(request.user) 
    return HttpResponseRedirect(request.META['HTTP_REFERER'])     




def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})





def profile(request):
   profile = Profile.objects.get(user=request.user)
   return render(request,'accounts/profile.html',{'profile':profile,})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        pass
    else:
        userform = UserForm()
        # profileform =ProfileForm()

    return render(request, 'accounts/profile_edit.html' , {'userform':UserForm, })

