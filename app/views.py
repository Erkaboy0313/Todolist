from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello world')

def hello(request,name):
    return HttpResponse(f'Hello {name}')

def age(request,name,age):
    return HttpResponse(f'hello I am {name}, I am {age} year old')

def page(request):
    return render(request,'index.html')