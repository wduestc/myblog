# coding:utf-8
__author__ = 'wduestc'
from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    #article = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles':articles})
    #return render(request, 'index.html', { 'hello':'Hello, Blog'})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article':article})

def edit_page(request, article_id):
    if str(article_id) == "0":
        return render(request, 'blog/edit_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'blog/edit_page.html', {'article':article})

def edit_action(request):
    id = request.POST.get('id', '0')
    if id == '0':
      title = request.POST.get('title', 'TITLE')
      content = request.POST.get('content', 'CONTENT')
      models.Article.objects.create(title=title, content=content)
      articles = models.Article.objects.all()
    else:
      title = request.POST.get('title', 'TITLE')
      content = request.POST.get('content', 'CONTENT')
      article = models.Article.objects.get(pk=id)
      article.title = title
      article.content = content
      article.save()
      articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles':articles})