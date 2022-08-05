from django.urls import path
from . views import index,items,create,lists,notfound

urlpatterns = [
    path('',index,name='index'),
    path('items/<int:id>/',items,name='items'),
    path('mylist/',lists,name='lists'),
    path('create/',create,name='create'),
    path('notfound/',notfound,name='notfound')
]