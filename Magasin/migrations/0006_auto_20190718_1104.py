# Generated by Django 2.2.3 on 2019-07-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Magasin', '0005_auto_20190718_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Date_C11',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='Date_C5',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='Date_OrdM',
            field=models.DateField(blank=True, null=True),
        ),
    ]
