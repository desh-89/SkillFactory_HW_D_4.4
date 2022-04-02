from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'

class PostDetail(DetailView):
    model = Post
    context_object_name = 'new'
    template_name = 'post_detail.html'