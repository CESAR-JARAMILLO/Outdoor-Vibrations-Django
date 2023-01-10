from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import BlogPost
from .forms import SubscribeForm

# Create your views here.
def index(request):
  return render(request, 'blog/index.html')

def about(request):
  return render(request, 'blog/about.html')

def thankyou(request):
  return render(request, 'blog/thankyou.html')

# def subscribe(request):
#   return render(request, 'blog/subscribe.html')

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)

        if form.is_valid():
            # name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # content = form.cleaned_data['content']

            html = render_to_string('blog/emails/subscribeform.html', {
                # 'name':name,
                'email':email,
                # 'content':content
            })

            send_mail('The contact form subject', 'This is the message', 'noreply@code.com', ['cesarjaramillodev@gmail.com'], html_message=html)

            return redirect('/thankyou/')
    else:
        form = SubscribeForm()
    
    return render(request, 'blog/subscribe.html', {'form':form})

def blog_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_post.html', {'post': post})

def blog_cards(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog/blog_cards.html', {'blog_posts': blog_posts})
