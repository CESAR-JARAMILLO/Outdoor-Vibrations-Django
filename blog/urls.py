from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('blog/<int:pk>/', views.blog_post, name='blog_post'),
    path('blog/cards/', views.blog_cards, name='blog_cards'),
    path('thankyou/', views.thankyou, name='thankyou'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
