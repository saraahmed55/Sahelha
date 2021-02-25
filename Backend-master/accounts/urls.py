

from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


app_name='tracksapp'

urlpatterns = [
    path('signup/',views.signup , name='signup'),
    path('profile/',views.profile , name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('profile/favourites/', views.favourite_list, name='favourite_list')
]