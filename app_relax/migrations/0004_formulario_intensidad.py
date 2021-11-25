# Generated by Django 3.0 on 2021-11-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0003_formulario_sentimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='intensidad',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
