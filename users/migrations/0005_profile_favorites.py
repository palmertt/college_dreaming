# Generated by Django 3.1.2 on 2020-11-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0026_auto_20201113_1623'),
        ('users', '0004_remove_profile_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favorite', to='universities.Institutions'),
        ),
    ]