from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from extensions.utils import jalali_converter
from accounts.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# comment
from django.contrib.contenttypes.fields import GenericRelation
from comment.models.comments import Comment
# end comment


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

    def search(self, query):
        return self.get_queryset()


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class TagManager(models.Manager):
    def published(self):
        return self.filter(active=True)


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.CASCADE,
                               related_name='children', verbose_name='زیر دسته')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')

    objects = CategoryManager()

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['position']

    def __str__(self):
        return self.title


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آدرس ip')

    class Meta:
        verbose_name = 'آدرس ip'
        verbose_name_plural = 'آدرس ip ها'

    def __str__(self):
        return self.ip_address


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
    )
    CONTENT_CHOICES = (
        ('a', 'مقاله'),
        ('n', 'خبر'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles',
                               verbose_name='نویسنده')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, verbose_name='آدرس')
    content_choice = models.CharField(max_length=1, choices=CONTENT_CHOICES, default='a', verbose_name='محتوا')
    description = RichTextUploadingField(verbose_name='متن')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته بندی')
    tags = models.ManyToManyField('Tag', related_name='articles',
                                  verbose_name='تگ ها / برچسب ها')
    image = models.ImageField(upload_to="images", verbose_name='تصویر شاخص مقاله')
    image_alt = models.CharField(max_length=100, blank=True, null=True, verbose_name='متن جایگزین تصویر شاخص')
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d', verbose_name='وضعیت')
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, through="ArticleHit", blank=True, related_name='hits',
                                  verbose_name='بازدید ها')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.id), self.slug])

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = 'تاریخ انتشار'

    def image_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px' src='{}'>".format(self.image.url))

    image_tag.short_description = "عکس مقاله"

    objects = ArticleManager()


class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان تگ')
    slug = models.SlugField(max_length=150, verbose_name='آدرس تگ')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name = 'تگ / برچسب'
        verbose_name_plural = 'نگ ها / برجسب ها'
        ordering = ['-created']

    def __str__(self):
        return self.title

    objects = TagManager()
