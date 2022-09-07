from django.db.models.query_utils import Q
from django.shortcuts import render
from blog.models import Article, Category
# from slider.models import Slider
from slider.models import Slider
from django.db.models import Count, Q
from datetime import datetime, timedelta


def home(request):
    last_month = datetime.today() - timedelta(days=30)
    last_week = datetime.today() - timedelta(days=7)
    context = {
        'articles': Article.objects.published().filter(content_choice='a'),
        'sliders': Slider.objects.all(),
        'last_news': Article.objects.published().filter(content_choice='n')[:4],
        'most_visited_articles_in_last_month': Article.objects.published().annotate(
            count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by
                                               ('-count', '-publish')[:8],
        'most_visited_articles_in_last_week': Article.objects.published().annotate(
            count=Count('hits', filter=Q(articlehit__created__gt=last_week))).order_by
                                              ('-count', '-publish')[:8],
    }
    return render(request, 'signalsafar/home.html', context)


def handle_404_error(request, exception):
    return render(request, '404.html', {})