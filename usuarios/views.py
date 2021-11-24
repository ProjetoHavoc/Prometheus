from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def lockout(request, credentials):
    return render( request, 'usuarios/erro403.html', status=403)    