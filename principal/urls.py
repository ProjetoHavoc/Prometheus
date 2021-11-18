from django.urls import path
from .views import PrincipalIndex

urlpatterns = [


    path('', PrincipalIndex, name='index'),
  
   

]