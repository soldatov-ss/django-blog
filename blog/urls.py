from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePosts.as_view(), name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('add_post/', add_post, name='add_post'),
    path('post/<int:pk>/', ViewPost.as_view(), name='view_post'),
    path('category/<int:category_id>/', get_category, name='category')
]
