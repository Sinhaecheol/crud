from django.shortcuts import render
from django.utils import timezone

from .models import Blog
# Create your views here.
def layout(request):
    return render(request, 'blog/layout.html')

def home(request):
    return render(request, 'blog/home.html')

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return render(request, 'blog/home.html')