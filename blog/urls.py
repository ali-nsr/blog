from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('blog', views.ArticleList.as_view(), name='article_list'),
    path('<int:article_id>/<str:slug>', views.detail, name='detail'),
    path('category/<slug:slug>', views.CategoryList.as_view(), name='category_list'),
    path('author/<slug:username>', views.AuthorList.as_view(), name='author'),
    path('search/', views.SearchList.as_view(), name='search'),
    path('tag/<slug:slug>', views.TagList.as_view(), name='tag_list'),
]
