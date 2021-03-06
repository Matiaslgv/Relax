# Generated by Django 3.0 on 2021-12-07 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0026_auto_20211207_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='detonante',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='intensidad',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='sentimiento',
            field=models.IntegerField(choices=[[0, 'Tristeza'], [1, 'Rabia'], [2, 'Angustia'], [3, 'Ansia'], [4, 'Miedo'], [5, 'Frustración'], [6, 'Verguenza']], default=2),
        ),
        migrations.AddField(
            model_name='profile',
            name='situacion',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='nota',
            name='timestamp',
            field=models.DateTimeField(default='2021-12-07 00:40'),
        ),
    ]
