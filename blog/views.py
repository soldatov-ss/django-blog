from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import F
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.views.generic.edit import DeleteView

from blog.forms import NewPost, UserRegisterForm, UserLoginForm
from blog.models import Post, Category


class HomePostsView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-created_at').select_related('category')


class PostView(DetailView):
    model = Post
    template_name = 'blog/view_post.html'
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()  # Чтобы выводилось корректное кол-во просмотров
        return context


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = NewPost
    raise_exception = True


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    raise_exception = True


class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = NewPost
    template_name = 'blog/add_post.html'
    raise_exception = True


class PostsByCategoryView(ListView):
    model = Post
    template_name = 'blog/home_category_list.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = str(Category.objects.get(pk=self.kwargs['category_id'])).title()
        return context

    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['category_id']).select_related('category')


class LoginUserView(LoginView):
    authentication_form = UserLoginForm
    next_page = 'home'


class RegisterUserView(CreateView):
    form_class = UserRegisterForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def user_logout(request):
    logout(request)
    return redirect('home')

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm()
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Вы успешно зарегестрировались')
#             return redirect('home')
#         else:
#             messages.error(request, 'Ошибка регистрации')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'blog/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserLoginForm()
#     return render(request, 'blog/login.html', {'form': form})
