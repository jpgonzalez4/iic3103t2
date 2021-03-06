# Generated by Django 3.0.5 on 2020-04-30 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0009_auto_20200430_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='descripcion',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hamburguesa',
            name='imagen',
            field=models.URLField(default='null'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hamburguesa',
            name='nombre',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hamburguesa',
            name='precio',
            field=models.PositiveIntegerField(),
        ),
    ]
