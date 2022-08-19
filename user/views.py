from multiprocessing import context
import re
from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import loginForm, registerForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def registerUser(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,'Registered Successfully')
        return redirect("index")
    context = {
        "form" : form
    }

    return render (request,"register.html",context)
def logIn(request):
    form = loginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        userControl = authenticate(username = username,password = password)
        if userControl is None:
            messages.info(request,'Username or Password Is Incorrect')
            return render(request,"login.html",context)
        
        messages.success(request,'Welcome '+ username + ' :)')
        login(request,userControl)
        return redirect("index")

    return render (request,"login.html",context)
def logOut(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect("index")
