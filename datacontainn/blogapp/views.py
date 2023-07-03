from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


from .forms import PostForm

from .models import Post

# Create your views here.
#def home(request):
#   return render(request, 'home.html',{'cats'})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request, 'categories.html',{'cats': cats,'category_posts': category_posts})



class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-details.html'


class PostArticleView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post-artical.html'
    #fields = '__all__'
    # fields = ('title','body')


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update-post.html'
    fields = ['title','title_tag','body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')