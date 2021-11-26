
from django.shortcuts import render, redirect, get_object_or_404
from blog_posts.models import Post
from django.views.generic.list import ListView




 

      

class index(ListView):
    
   model = Post #model usado para preencher 
   template_name = 'administracao/index-admin.html'#direcionando para o template
   #paginate_by = 6 # quantos posts vao ficar na pagina
   context_object_name = 'posts'#objeto de busca
   
   #funcao para colocar os posts em ordem do ultimo adicionado(mais recente)
   def get_queryset(self):
       qs = super().get_queryset()# refazendo o query set com a variavel qs
       qs = qs.order_by('-id')
       
   

       return qs
    
   

    


def Sobre(request):


    return render(request, 'administracao/login.html')