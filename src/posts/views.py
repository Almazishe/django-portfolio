from django.shortcuts import render
from django.views.generic import ListView

from .forms import PostListForm
from .models import Post



class PostListView(ListView):
    """ Лист постов / Главная стр """

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset