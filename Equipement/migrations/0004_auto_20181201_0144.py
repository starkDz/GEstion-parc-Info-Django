# Generated by Django 2.1.2 on 2018-12-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipement', '0003_service_service_per'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systeme',
            name='Type',
            field=models.CharField(default='/', max_length=250),
        ),
    ]
