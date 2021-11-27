
from django.shortcuts import render,  get_object_or_404
from blog_posts.models import Post
from blog_posts.forms import PostForm




 

    

def index(request):
    
    posts = Post.objects.all()



    return render(request, 'administracao/index-admin.html', context ={"index":  "Index",
                                                   "posts": posts, })


def post_detalhes(request, id):

    post = get_object_or_404(Post, id=id)

    

    if request.method == "POST":

        form = PostForm(request.POST, instance=post)

     

    

    return render(request, "blog_posts/post_detalhes.html", context = {"form":form})


   

    


def erro401(request):


    return render(request, 'administracao/erro401.html')

def erro403(request):


    return render(request, 'administracao/erro403.html')


def erro404(request):
    

    return render(request, 'administracao/erro404.html')


def erro500(request):
    

    return render(request, 'administracao/erro500.html')


def esqueceu(request):
    

    return render(request, 'administracao/esqueceu.html')


def login(request):
    

    return render(request, 'administracao/login.html')



    