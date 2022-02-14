# Generated by Django 3.0 on 2022-02-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20220211_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default='2021-02-11', verbose_name='Время создание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='datetime_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время удаление'),
        ),
        migrations.AddField(
            model_name='group',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Время обновление'),
        ),
    ]
