# Generated by Django 3.1.2 on 2020-11-13 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorites',
        ),
    ]