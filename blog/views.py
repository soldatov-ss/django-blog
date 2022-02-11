from django.db.models import F
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from blog.models import Post, Category


class HomePosts(ListView):
    '''
    def home(request):
        posts = Post.objects.all()
        return render(request, 'blog/home.html', {'posts': posts})
    '''
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class ViewPost(DetailView):
    '''
    def view_post(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'blog/view_post.html', {'post': post})
    '''
    model = Post
    template_name = 'blog/view_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db() # Чтобы выводилось корректное кол-во просмотров
        return context


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


def get_category(request):
    pass
