# Generated by Django 2.1 on 2018-08-28 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_journeyphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Відгук')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.Journey')),
                ('user', models.ForeignKey(on_delete=False, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]