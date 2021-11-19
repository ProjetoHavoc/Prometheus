from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['titulo_post', 'excerto_post', 'conteudo_post', 'autor_post', 'categoria_post', 'imagem_post']

        widgets = {
            
            'titulo_post': forms.TextInput(attrs={'placeholder':'Titulo', 'class': 'form-control form-control-lg'}),
            'excerto_post': forms.TextInput(attrs={'placeholder':'Súmario', 'class': 'form-control form-control-lg'}),
            'conteudo_post':SummernoteWidget(),
            #'Conteúdo': forms.Textarea(attrs={'placeholder':'Conteúdo', 'class': 'form-control form-control-lg'}),
            'autor_post': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            'categoria_post': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            'imagem_post': forms.FileInput(attrs={'id':'validatedCustomFile'}),
        }


#class PostForm(forms.ModelForm):

    

    #content = forms.CharField(widget=SummernoteWidget())

    #class Meta:
        #model = Post

        #conteudo_post = forms.CharField(widget=SummernoteWidget())

        
        #fields = ['titulo_post', 'excerto_post', 'autor_post', 'categoria_post', 'imagem_post']

        #widgets = {
            
          #  'Titulo': forms.TextInput(attrs={'placeholder':'Titulo', 'class': 'form-control form-control-lg'}),
         #   'Sumário': forms.Textarea(attrs={'placeholder':'Súmario', 'class': 'form-control form-control-lg'}),
            #'Conteúdo':forms.CharField(label='iframe', widget=SummernoteWidget()),
            #'Conteúdo': forms.Textarea(attrs={'placeholder':'Conteúdo', 'class': 'form-control form-control-lg'}),
            #'Autor': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            #'Categoria': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            #'imagem': forms.FileInput(attrs={'id':'validatedCustomFile'}),
        #}

