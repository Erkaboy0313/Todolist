from django.urls import path
from . views import index,items,create,lists,handle_items

urlpatterns = [
    path('',index,name='index'),
    path('items/<int:id>/',items,name='items'),
    path('mylist/',lists,name='lists'),
    path('create/',create,name='create'),
    path('handle_items/<int:id>',handle_items,name='handle_items')
]