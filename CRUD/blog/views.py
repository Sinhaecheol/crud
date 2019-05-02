from django.shortcuts import render
from django.utils import timezone

from .models import Blog
# Create your views here.
def layout(request):
    return render(request, 'blog/layout.html')

def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})
