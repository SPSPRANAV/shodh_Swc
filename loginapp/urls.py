from django.urls import path
from django.contrib import admin

from loginapp import views as loginapp_views

urlpatterns = [
    path('', loginapp_views.login, name='login'),
]