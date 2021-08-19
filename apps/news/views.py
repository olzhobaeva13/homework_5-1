from django.shortcuts import render
from django.views.generic import View, DetailView
from .models import Post

class MainPageView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'news/main_page.html', context={'posts': posts})

class NewsDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/news_detail.html'
