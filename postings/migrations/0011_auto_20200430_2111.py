# Generated by Django 3.0.5 on 2020-05-01 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0010_auto_20200430_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hamburguesa',
            name='imagen',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='hamburguesa',
            name='precio',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]