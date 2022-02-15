from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePostsView.as_view(), name='home'),
    path('logout/', user_logout, name='user_logout'),
    path('login/', LoginUserView.as_view(), name='user_login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('add_post/', CreatePostView.as_view(), name='add_post'),
    path('post/<int:pk>/', PostView.as_view(), name='view_post'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('category/<int:category_id>/', PostsByCategoryView.as_view(), name='category_list')
]
