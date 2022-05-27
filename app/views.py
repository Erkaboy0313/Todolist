from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import UserList,Item
from .forms import CreateList

# Create your views here.

def index(request):
    lists = UserList.objects.all()
    context = {
        'lists':lists
    }
    return render(request,'index.html',context)

def items(request,id):
    list = UserList.objects.get(id = id)
    items = Item.objects.filter(list_name = list)
    context = {
        'list':list,
        'items':items
    }
    return render(request,'items.html',context)

def create(request):
    if request.method == "POST":
        form = CreateList(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            UserList.objects.create(name = name)

        # name = request.POST.get('name')
            return redirect('index')
        else:
            return HttpResponse('Some thing went wrong')
    form = CreateList()
    return render(request,'create.html',{'form':form})