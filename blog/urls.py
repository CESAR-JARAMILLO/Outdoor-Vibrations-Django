from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:pk>/', views.blog_post, name='blog_post'),
    path('blog/cards/', views.blog_cards, name='blog_cards'),
]
