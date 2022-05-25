from django.urls import path
from . views import hello, index, age,page

urlpatterns = [
    path('',index,name='index'),
    path('page/',page,name='page'),
    path('<str:name>/',hello,name='hello'),
    path('<str:name>/<int:age>/',age,name='age'),
]