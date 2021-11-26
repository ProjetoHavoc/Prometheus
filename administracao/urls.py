from django.urls import path
from administracao.views import  index, erro401, erro403, erro404, erro500, esqueceu, login

urlpatterns = [


    path('', index, name='index'),
    path('erro401/', erro401, name='erro401'),
    path('erro403/', erro403, name='erro403'),
    path('erro404/', erro404, name='erro404'),
    path('erro500/', erro500, name='erro500'),  
    path('esqueceu/', esqueceu, name='esqueceu'),
    path('login/', login, name='login'),
    
   


]