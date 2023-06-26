from ast import Delete
from ctypes.wintypes import POINT
from importlib.resources import contents
from multiprocessing import context
from operator import ge
from pydoc import visiblename
from turtle import title
from venv import create
from webbrowser import get
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts= Post.objects.all()
        context= {
            'posts':posts

        }
        return render(request, 'blog_list.html', context)


class BlogCreateView(View):

    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context= {
            'form':form

        }
        return render (request, 'blog_create.html', context)
    

    # Se requiere un metodo post para enviar toda la informacion de lo que ingrese el usuario. 
    def post(self, request, *args, **kwargs): 
        if request.method == "POST":
            form= PostCreateForm(request.POST)
        if form.is_valid():                          # Si  el contenido es valido la informacion se procede a enviar el titulo y contenido
            title= form.cleaned_data.get('title')
            contents = form.cleaned_data.get('contents')

            p, create = Post.objects.get_or_create(title=title,contents=contents)
            p.save()
            return redirect('blog:home')

        context= {

        }
        return render (request, 'blog_create.html', context)


class BlogDetailsView(View):
    def get(self, request,pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context={
            'post':post

        }
        return render (request, 'blog_detail.html', context)


class BlogUpdateView(UpdateView):
    model=Post
    fields=['title', 'contents']
    template_name= 'blog_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs= {'pk':pk})


class BlogDeleteView(DeleteView):
    model=Post
    template_name= 'blog_delete.html'
    success_url= reverse_lazy('blog:home')

