# Generated by Django 2.2.16 on 2023-02-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20230221_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(help_text='Введите текст', verbose_name='Тело коммента'),
        ),
    ]