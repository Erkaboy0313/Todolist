from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import UserList,Item
from .forms import CreateList


# Create your views here.

def index(request):

    return render(request,'index.html')

def notfound(request):
    return render(request,'404.html')

def lists(request):
    if request.user.is_authenticated:
        lists = UserList.objects.filter(user = request.user)
    else:
        lists = []
    context = {
        'lists':lists
    }
    return render(request,'mylist.html',context)


def items(request,id):
    list = UserList.objects.get(id = id)
    context = {
        'list':list,
    }
    return render(request,'list.html',context)

def create(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = CreateList(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                UserList.objects.create(user = request.user, name = name)

            # name = request.POST.get('name')
                return redirect('index')
            else:
                return HttpResponse('Some thing went wrong')
        else:
            return redirect('login')
    form = CreateList()
    return render(request,'create.html',{'form':form})
