# Generated by Django 3.1 on 2020-09-05 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='gpa',
            field=models.CharField(default=3.0, max_length=5),
            preserve_default=False,
        ),
    ]
