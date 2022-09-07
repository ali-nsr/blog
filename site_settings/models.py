from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class SiteSettings(models.Model):
    header_logo = models.ImageField(upload_to='images/logo', null=True, blank=True, verbose_name='تصویر لوگوی هدر')
    footer_logo = models.ImageField(upload_to='images/logo', null=True, blank=True, verbose_name='تصویر لوگوی فوتر')
    fav_logo = models.ImageField(upload_to='images/logo', null=True, blank=True, verbose_name='لوگوی نوبار')
    office_address = models.CharField(max_length=300, blank=True, null=True, verbose_name='آدرس دفتر')
    office_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='شماره تلفن دفتر')
    office_fax = models.CharField(max_length=50, blank=True, null=True, verbose_name='شماره فکس دفتر')
    office_email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='ایمیل دفتر')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return 'تنظیمات'


class AboutUs(models.Model):
    text = RichTextUploadingField(blank=True, null=True, verbose_name='متن')

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'ویرایش درباره ما'

    def __str__(self):
        return 'درباره ما'
