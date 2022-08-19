from atexit import register
from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "user"

urlpatterns = [
    path('register/',views.registerUser,name = "register"),
    path('login/',views.logIn,name = "login"),
    path('logout/',views.logOut,name = "logout"),
]