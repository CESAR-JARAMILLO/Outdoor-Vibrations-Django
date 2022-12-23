from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def index(request):
  return render(request, 'blog/index.html')

def blog_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_post.html', {'post': post})

def blog_cards(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog/blog_cards.html', {'blog_posts': blog_posts})
