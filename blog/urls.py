from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePostsView.as_view(), name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('add_post/', CreatePostView.as_view(), name='add_post'),
    path('post/<int:pk>/', PostView.as_view(), name='view_post'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('category/<int:category_id>/', get_category, name='category')
]
