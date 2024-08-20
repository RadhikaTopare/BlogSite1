from django.shortcuts import render
from .models import BlogPost, Category, Comment

# Create your views here.

def blog_home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_home.html', {'posts': posts})

def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})