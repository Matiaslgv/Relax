# Generated by Django 3.0 on 2021-12-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0008_auto_20211201_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cuatro_mes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='dos_mes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='quinto_mes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='septimo_mes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='sexto_mes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='tres_mes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='un_mes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='howdoyoufeel',
            name='algo',
            field=models.CharField(blank=True, default='&', max_length=10000),
        ),
    ]
