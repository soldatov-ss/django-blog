from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

from blog.models import Post, Category


class HomePosts(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class PostsByCategory(ListView):
    model = Category
    template_name = 'blog/home.html'
    context_object_name = 'categories'

def login(request):
    pass


def register(request):
    pass


def add_post(request):
    pass
