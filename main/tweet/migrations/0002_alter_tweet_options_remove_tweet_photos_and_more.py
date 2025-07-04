# Generated by Django 5.2.3 on 2025-07-03 04:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-created_at'], 'verbose_name': 'Tweet', 'verbose_name_plural': 'Tweets'},
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='photos',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TweetPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics/')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='tweet.tweet')),
            ],
            options={
                'verbose_name': 'Tweet Photo',
                'verbose_name_plural': 'Tweet Photos',
            },
        ),
    ]
