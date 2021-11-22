from django.urls import path
from .views import PrincipalIndex, Sobre

urlpatterns = [


    path('', PrincipalIndex, name='index'),
    path('sobre/', Sobre, name='sobre'),
  
   

]