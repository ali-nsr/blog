# Generated by Django 3.2.4 on 2021-07-16 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210716_0722'),
        ('blog_tag', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
