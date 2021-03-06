# Generated by Django 3.2.3 on 2021-06-15 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0019_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='time',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
