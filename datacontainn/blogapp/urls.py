

from django.urls import path
#from . import views 

from .views import HomeView, ArticleDetailView,PostArticleView,UpdatePostView,DeletePostView,CategoryView,AddCategoryView, CategoryListView,LikeView

urlpatterns = [
    #path('',views.home, name='h'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-details'),
    path('add_post/',PostArticleView.as_view(), name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name='delete_post'),
    path('category/<str:cats>/', CategoryView,name= 'category'),
    path('add_category/', AddCategoryView.as_view(),name='add_category'),
    path('category-list/', CategoryListView,name= 'category_list'),
    path('like/<int:pk>/',LikeView, name='like_post'),
]
