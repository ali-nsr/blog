from django.shortcuts import render, get_object_or_404
from accounts.models import User
from django.views.generic import ListView
from .models import Article, Category, Tag
from django.db.models import Q


def detail(request, article_id, slug):
    article = get_object_or_404(Article, id=article_id, slug=slug, status='p')
    context = {
        'article': article,
        'tags': Tag.objects.all(),
        'last_news': Article.objects.published().filter(content_choice='n')[:6],
    }

    ip_address = request.user.ip_address
    if ip_address not in article.hits.all():
        article.hits.add(ip_address)

    return render(request, 'blog/detail.html', context)


class CategoryList(ListView):
    template_name = 'blog/category_list.html'
    paginate_by = 8

    def get_queryset(self):
        global last_news
        last_news = Article.objects.published().filter(content_choice='n')[:5]
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'category': category,
            'last_news': last_news,
        })
        return context


class ArticleList(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    paginate_by = 8

    def get_queryset(self):
        global last_news
        last_news = Article.objects.published().filter(content_choice='n')[:5]
        return Article.objects.published().filter(content_choice='a')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_news'] = last_news
        return context


class AuthorList(ListView):
    template_name = 'blog/author_list.html'
    paginate_by = 8

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context


class SearchList(ListView):
    template_name = 'blog/search_list.html'
    paginate_by = 8

    def get_queryset(self):
        global last_news
        last_news = Article.objects.published().filter(content_choice='n')[:5]
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Article.objects.filter(
                Q(description__icontains=query) |
                Q(title__icontains=query) |
                Q(tags__title__icontains=query)
            ).distinct()
        return Article.objects.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'search': self.request.GET.get('q'),
                'last_news': last_news,
            }
        )
        return context


class TagList(ListView):
    template_name = 'blog/tag_list.html'
    paginate_by = 8

    def get_queryset(self):
        global tag
        slug = self.kwargs.get('slug')
        tag = get_object_or_404(Tag.objects.published(), slug=slug)
        return tag.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = tag
        return context
