from django import template
from blog.models import Category, Article
from accounts.models import User
from site_settings.models import SiteSettings

from django.db.models import Count, Q
from datetime import datetime, timedelta

register = template.Library()


@register.simple_tag
def title():
    return 'سیگنا سفر'


@register.inclusion_tag('partials/category_navbar.html')
def category_navbar():
    return {
        'category': Category.objects.filter(status=True),
        'user': User
    }


@register.inclusion_tag('partials/footer_settings.html')
def footer_settings():
    last_month = datetime.today() - timedelta(days=30)
    return {
        'site_settings': SiteSettings.objects.first(),
        'categories': Category.objects.filter(status=True)[:8],
        'most_visited_articles_in_last_month': Article.objects.published().annotate(
            count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by
                                               ('-count', '-publish')[:4],
    }


@register.inclusion_tag('partials/header_settings.html')
def header_settings():
    return {
        'site_settings': SiteSettings.objects.first(),
    }


@register.inclusion_tag('partials/nav_logo.html')
def nav_logo():
    return {
        'site_settings': SiteSettings.objects.first(),
    }


@register.inclusion_tag('partials/latest_news.html')
def latest_news():
    return {
        'last_news': Article.objects.published().filter(content_choice='n')[:4],
    }
