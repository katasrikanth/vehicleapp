# Generated by Django 3.2.8 on 2021-10-31 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0005_auto_20211031_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
