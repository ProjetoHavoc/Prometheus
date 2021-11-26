from django.urls import path
from administracao import views
from .views import  Sobre

urlpatterns = [


    path('', views.index.as_view(), name='blog_index'),
    path('sobre/', Sobre, name='sobre'),
  
   

]