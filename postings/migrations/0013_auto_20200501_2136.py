# Generated by Django 3.0.5 on 2020-05-02 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0012_auto_20200430_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hamburguesa',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ingrediente',
            name='id',
        ),
        migrations.AddField(
            model_name='hamburguesa',
            name='hamburguesa_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='ingredient_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
