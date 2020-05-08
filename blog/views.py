from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    blog = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blog})


def detail(request, blog_id):
    return render(request, 'blog/detail.html', {'id':blog_id})
    