# Generated by Django 2.1.2 on 2018-12-27 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reseaux', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipement',
            name='etat_equipement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipement.Etat'),
        ),
    ]