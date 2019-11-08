from django.urls import path,include
from . import views
from django.views.generic import TemplateView
from .models import Intern_Model


app_name= 'student'

urlpatterns = [
    path('', views.index , name='index'),
    path('', include('stud_profile.urls')),
    path('apply', views.apply , name='apply'),
    path('profile', views.profile , name='profile'),
]
