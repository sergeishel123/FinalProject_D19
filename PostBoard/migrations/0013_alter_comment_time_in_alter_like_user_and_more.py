# Generated by Django 4.1.4 on 2023-01-18 03:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PostBoard', '0012_remove_like_post_like_comment_alter_comment_time_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 18, 3, 22, 44, 173275)),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 18, 3, 22, 44, 173275)),
        ),
    ]
