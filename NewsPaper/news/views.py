from django.shortcuts import render
from news.models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse

class PostList(ListView):
    model = Post
    context_object_name = 'Posts'
    template_name = 'news/default.html'
    #queryset = Post.objects.all()


def detail(request, pk):
    post = Post.objects.get(pk__iexact=pk)
    return render(request, 'detail.html', context={'post': post})

# class Post(DetailView):
#     model = Post
#     context_object_name = 'Post'
#     template_name = 'news/detail.html'


# def default(request):
#      posts = Post.objects.all()
#      return render(request, 'default.html', context={'posts': posts})
#






# class PostCreate(CreateView):
#     model = Post
#     field = '__all__'