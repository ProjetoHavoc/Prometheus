
from django.shortcuts import render, redirect, get_object_or_404


def index(request):

    
   

    return render(request, 'administracao/index.html')


def Sobre(request):


    return render(request, 'principal/sobre.html')