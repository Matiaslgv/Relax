# Generated by Django 3.0 on 2021-12-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0018_nota_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='content',
            field=models.TextField(),
        ),
    ]
