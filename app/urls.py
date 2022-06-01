from django.urls import path
from . views import index,items,create,lists

urlpatterns = [
    path('',index,name='index'),
    path('items/<int:id>/',items,name='items'),
    path('mylist/',lists,name='lists'),
    path('create/',create,name='create')
]