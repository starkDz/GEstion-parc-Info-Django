# Generated by Django 2.2.3 on 2019-07-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Magasin', '0004_auto_20190717_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Date_C12',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='Date_C7',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='Num_C11',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='Num_C12',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='Num_C5',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='Num_C7',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='Num_OrdM',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
