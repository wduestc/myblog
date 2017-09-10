#!/usr/bin/env python
# coding:utf-8
# @Time     : 17-9-10 上午9:54
# @Author   : w_di_sc
# @Site     : 
# @File     : urls.py
# @Software : PyCharm
from django.conf.urls import url, include
from django.contrib import admin
from . import views
#from  blog.views import index

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit_page/$', views.edit_page, name='edit_page'),
    url(r'^edit/action/$', views.edit_action, name='edit_action')
]