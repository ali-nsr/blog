# Generated by Django 4.1.1 on 2022-09-07 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_1', to='blog.article', verbose_name='اسلایدر اول')),
                ('slider_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_2', to='blog.article', verbose_name='اسلایدر دوم')),
                ('slider_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_3', to='blog.article', verbose_name='اسلایدر سوم')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
    ]