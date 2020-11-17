# Generated by Django 3.1.2 on 2020-11-12 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('universities', '0019_auto_20201112_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutions',
            name='favorites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]