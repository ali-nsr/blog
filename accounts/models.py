from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    profile_image = models.ImageField(upload_to='profile', null=True, blank=True, verbose_name='تصویر پروفایل')
