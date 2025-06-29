from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('author/<int:author_id>/', views.posts_by_author, name='posts_by_author'),
    path('create/', views.create_post, name='create_post'),

]
