# Generated by Django 2.1.2 on 2019-07-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipement', '0014_remove_materiel_categorie_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='Address_Mac',
            field=models.CharField(max_length=30),
        ),
    ]
