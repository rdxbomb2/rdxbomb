from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about', views.about,name='about'),
    path('powerfulindex', views.powerfulindex,name='powerfulindex'),
    path('powerfulattack', views.powerfulattack,name='powerfulattack'),
    path('register', views.register,name='register'),
    path('help', views.help,name='help'),
    path('adduser', views.adduser,name='adduser'),
    path('useradded', views.useradded,name='useradded'),
    path('doattack/', views.doattack,name="doattack")

]