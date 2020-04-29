# Generated by Django 3.0.5 on 2020-04-26 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0003_auto_20200425_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hamburguesa',
            name='creation',
        ),
        migrations.RemoveField(
            model_name='hamburguesa',
            name='description',
        ),
        migrations.RemoveField(
            model_name='hamburguesa',
            name='image',
        ),
        migrations.RemoveField(
            model_name='hamburguesa',
            name='name',
        ),
        migrations.RemoveField(
            model_name='hamburguesa',
            name='price',
        ),
        migrations.RemoveField(
            model_name='ingrediente',
            name='creation',
        ),
        migrations.RemoveField(
            model_name='ingrediente',
            name='description',
        ),
        migrations.RemoveField(
            model_name='ingrediente',
            name='name',
        ),
        migrations.AddField(
            model_name='hamburguesa',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hamburguesa',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hamburguesa',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hamburguesa',
            name='precio',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
