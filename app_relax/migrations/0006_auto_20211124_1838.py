# Generated by Django 3.0 on 2021-11-24 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0005_formulario_detonante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='sentimento',
        ),
        migrations.AddField(
            model_name='formulario',
            name='sentimiento',
            field=models.IntegerField(choices=[[0, 'Tristeza'], [1, 'Rabia'], [2, 'Angustia'], [3, 'Ansia'], [4, 'Miedo'], [5, 'Frustración'], [6, 'Verguenza']], default=2),
        ),
    ]
