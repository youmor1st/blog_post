from django.urls import path
from .views import post_detail, post_list, post_create, post_edit, post_delete, add_comment_to_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/edit/<int:pk>/', post_edit, name='post_edit'),
    path('post/delete/<int:pk>/', post_delete, name='post_delete'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
]
