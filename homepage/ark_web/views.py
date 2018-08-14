from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post, News, Idea

# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pub_date')
    content = { 'posts':posts}
    return render(request, 'ark_web/index.html', content)


def gallery(request):
    posts = Post.objects.order_by('-pub_date')    
    content = {'posts':posts}
    return render(request, 'ark_web/gallery.html', content)


def about(request):
    content = {}
    return render(request, 'ark_web/about.html', content)


def news(request):
    newss = News.objects.order_by('-pub_date')    
    content = {'newss':newss}
    return render(request, 'ark_web/news.html', content)


def idea(request):
    ideas = News.objects.order_by('-pub_date')    
    content = {'ideas':ideas}
    return render(request, 'ark_web/idea.html', content)


def progress(request):
    content = {}
    return render(request, 'ark_web/progress.html', content)
