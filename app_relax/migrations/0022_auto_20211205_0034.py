# Generated by Django 3.0 on 2021-12-05 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0021_auto_20211204_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='fecha',
            field=models.CharField(default='2021-12-05', max_length=200),
        ),
    ]
