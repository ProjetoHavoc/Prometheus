from django.urls import path
from blog_categorias import views

urlpatterns = [

    path('', views.CategoriasIndex.as_view(), name='categoria_index'),
    path('animes/', views.Animes.as_view(), name='animes'),
    path('tecnologia/', views.Tecnologia.as_view(), name='tecnologia'),
    path('tutoriais/', views.Tutoriais.as_view(), name='tutoriais'),
    path('games/', views.Games.as_view(), name='games'),
    path('filmes/', views.Filmes.as_view(), name='filmes'),
   

]