# Generated by Django 3.2.8 on 2021-10-31 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0002_auto_20211031_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='Temperature',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='avgspeed',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='enginestats',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='fuellevel',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='speed',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
    ]
