from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import *

def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'title': 'Main page',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'About me'})

def addpage(request):
    return HttpResponse('Complete!')

def contact(request):
    return HttpResponse('Complete!')

def login(request):
    return HttpResponse('Complete!')

def show_post(request, post_id):
    post = get_object_or_404(Women, pk=post_id)

    context = {
        'posts': post,
        'title': post.title,
        'cat_selected': 1,
    }

    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)