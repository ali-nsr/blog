# Generated by Django 4.1.1 on 2022-09-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=150, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=200, verbose_name='عنوان پیام')),
                ('text', models.TextField(verbose_name='متن پیام')),
                ('is_read', models.BooleanField(default=False, verbose_name='خوانده شده / نشده')),
            ],
            options={
                'verbose_name': 'تماس کاربر',
                'verbose_name_plural': 'تماس های کاربران',
            },
        ),
    ]
