

from django.shortcuts import render, redirect, get_object_or_404
from blog_posts.models import Post

def PrincipalIndex(request):

    posts = Post.objects.filter()
    
   

    return render(request, 'principal/index.html', {'posts':posts})