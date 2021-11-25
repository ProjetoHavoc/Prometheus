from django.urls import path
from .views import index, Sobre

urlpatterns = [


    path('', index, name='index'),
    path('sobre/', Sobre, name='sobre'),
  
   

]