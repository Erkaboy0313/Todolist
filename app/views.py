from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import UserList,Item
from .forms import CreateList
from django.contrib import messages

def index(request):

    return render(request,'index.html')

def lists(request):
    if request.user.is_authenticated:
        lists = UserList.objects.filter(user = request.user)
    else:
        lists = []
    context = {
        'lists':lists
    }
    return render(request,'mylist.html',context)

def handle_items(request,id):
    if request.method == "POST":
        list = UserList.objects.get(id = id)
        if request.POST.get('save'):
            for item in list.item_set.all():
                if request.POST.get('s'+str(item.id)) == 'clicked':
                    item.is_done = True
                else:
                    item.is_done = False
                item.save()
        if request.POST.get('newItem'):
            name = request.POST.get('new')
            if len(name)>0:
                Item.objects.create(list_name = list,name = name,is_done = False)
        if request.POST.get('delate'):
            name = request.POST.get('new')
            try:
                Item.objects.get(name = name).delete()
            except:
                messages.add_message(request,messages.ERROR,'Item topilmadi')
        return redirect(f'/items/{id}')

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
                try:
                    UserList.objects.create(user = request.user, name = name)
                except:
                    messages.add_message(request,messages.ERROR,name='List yaratilmadi')
                    return redirect('create')
                return redirect('index')
            else:
                return HttpResponse('Some thing went wrong')
        else:
            return redirect('login')
    form = CreateList()
    return render(request,'create.html',{'form':form})
