
from django.urls import path ,include
from . import views

app_name='tracksapp'

urlpatterns = [
    
    path('',views.track_list, name = 'track_list'),
    path('tracks/<str:slug>',views.track_detail, name = 'track_detail'),

]