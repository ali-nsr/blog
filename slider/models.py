from django.db import models
from blog.models import Article


class Slider(models.Model):
    slider_1 = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='article_1',
                                 verbose_name='اسلایدر اول')
    slider_2 = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='article_2',
                                 verbose_name='اسلایدر دوم')
    slider_3 = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='article_3',
                                 verbose_name='اسلایدر سوم')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return 'اسلایدر'
