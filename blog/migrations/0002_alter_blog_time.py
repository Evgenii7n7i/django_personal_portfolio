# Generated by Django 4.1.7 on 2023-07-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
    ]
