# Generated by Django 2.1.2 on 2018-12-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipement', '0004_auto_20181201_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marque',
            name='Pays',
            field=models.CharField(default='/', max_length=20),
        ),
    ]