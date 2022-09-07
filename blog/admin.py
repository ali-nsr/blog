from django.contrib import admin
from .models import Article, Category, IPAddress, Tag
from accounts.models import User


def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "منتشر شد."
    else:
        message_bit = "منتشر شدند."
    modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))


make_published.short_description = "انتشار مقالات انتخاب شده"


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "پیش نویس شد."
    else:
        message_bit = "پیش نویس شدند."
    modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))


make_draft.short_description = "پیش نویس شدن مقالات انتخاب شده"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_field = ('title', 'slug')


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = User.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    list_display = ('title', 'content_choice', 'image_tag', 'slug', 'jpublish', 'author', 'status', 'category_to_str')
    list_filter = ('publish', 'content_choice', 'status')
    search_field = ('title', 'description')
    actions = [make_published, make_draft]
    ordering = ('-status', '-publish')

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.active()])

    category_to_str.short_description = 'دسته بندی'


admin.site.register(Article, ArticleAdmin)

admin.site.site_header = 'مدیریت سیگنال سفر'

admin.site.register(IPAddress)

admin.site.register(Tag)
