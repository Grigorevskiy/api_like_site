# Generated by Django 2.1 on 2018-08-28 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_news_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsphoto',
            name='news',
        ),
        migrations.DeleteModel(
            name='NewsPhoto',
        ),
    ]
