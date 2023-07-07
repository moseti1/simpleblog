from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect


from .forms import PostForm

from .models import Post,Category

# Create your views here.
#def home(request):
#   return render(request, 'home.html',{'cats'})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    ordering = ['-post_date']


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False 
    if post.like.filter(id=request.user.id).exists():

        post.likes.remove(request.user)
    else: 
        post.likes.add(request.user)
        liked = True

    post.likes.add(request.user)

    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html',{'cat_menu_list': cat_menu_list})


def CategoryView(request,cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request, 'categories.html',{'cats': cats.title(),'category_posts': category_posts})



class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()

        likes = get_object_or_404(Post, id= self.kwargs['pk'])

        total_likes = likes.total_likes()

        liked = False
        if likes.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


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


class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add-category.html'
    fields = '__all__'
    # fields = ('title','body')
    

