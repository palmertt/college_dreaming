# Generated by Django 3.1.2 on 2020-10-26 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0011_auto_20201025_2227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cities',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='institutions',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='zipcodes',
            options={'managed': True},
        ),
    ]