# Generated by Django 3.2.8 on 2021-10-31 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0004_auto_20211031_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image1',
            field=models.ImageField(upload_to='vehicleimg/image1'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image2',
            field=models.ImageField(upload_to='vehicleimg/image2'),
        ),
    ]
