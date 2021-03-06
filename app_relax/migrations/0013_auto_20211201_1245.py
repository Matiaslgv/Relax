# Generated by Django 3.0 on 2021-12-01 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_relax', '0012_auto_20211201_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='howdoyoufeel',
            name='algo',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='howdoyoufeel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='howdoyoufeel', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Como_estuvo_tu_dia',
            field=models.IntegerField(choices=[[0, 'Bueno'], [1, 'Decente'], [2, 'Normal'], [3, 'Malo'], [4, 'Terrible']], default='', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='algo',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
    ]
