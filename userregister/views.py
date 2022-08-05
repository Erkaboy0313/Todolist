from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegisterForm
from app.forms import Loginform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.errors:
            messages.add_message(request,messages.WARNING,form.errors)
        else:
            form.save()
            return redirect('login')

    form = RegisterForm()
    context = {
        'form':form
    }
    return render(request,'register/register.html',context)

def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request,username=username,password=password)
        if user:
            login(request=request,user=user)
            return redirect('index')
        else:
            messages.add_message(request,messages.WARNING,'User not found')
    form = Loginform()
    return render(request,'register/login.html',{'form':form})

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')