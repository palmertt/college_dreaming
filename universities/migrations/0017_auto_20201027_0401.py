# Generated by Django 3.1.2 on 2020-10-27 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0016_auto_20201027_0348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admissions',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='cities',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='completionrates',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='costs',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='institutions',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='institutiontypes',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='majors',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='programs',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='undergraduates',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='zipcodes',
            options={'managed': False},
        ),
    ]