from django.db.models import F
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from blog.forms import NewPost
from blog.models import Post, Category


class HomePostsView(ListView):
    '''
    def home(request):
        posts = Post.objects.all()
        return render(request, 'blog/home.html', {'posts': posts})
    '''
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class PostView(DetailView):
    '''
    def view_post(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'blog/view_post.html', {'post': post})
    '''
    model = Post
    template_name = 'blog/view_post.html'
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db() # Чтобы выводилось корректное кол-во просмотров
        return context



class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = NewPost
    success_url = reverse_lazy('home') # поправить


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')


class PostsByCategoryView(ListView):
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
