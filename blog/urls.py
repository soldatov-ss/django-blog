from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePosts.as_view(), name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('add_post/', add_post, name='add_post'),
]
