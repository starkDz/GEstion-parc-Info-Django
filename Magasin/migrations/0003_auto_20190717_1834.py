# Generated by Django 2.2.3 on 2019-07-17 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Magasin', '0002_auto_20190717_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Service_FK',
            field=models.ForeignKey(default='60', on_delete=django.db.models.deletion.CASCADE, to='Equipement.Service'),
        ),
    ]