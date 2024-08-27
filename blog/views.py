from django.shortcuts import render, redirect
from .models import BlogPost, Category, Comment
from .forms import PostForm

# Create your views here.

def blog_home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_home.html', {'posts': posts})

def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')  # Redirect to the homepage after saving
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})