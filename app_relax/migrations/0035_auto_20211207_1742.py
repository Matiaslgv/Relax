# Generated by Django 3.0 on 2021-12-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0034_auto_20211207_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='detonante',
            new_name='trigger',
        ),
        migrations.AlterField(
            model_name='nota',
            name='timestamp',
            field=models.DateTimeField(default='2021-12-07 17:42'),
        ),
    ]
