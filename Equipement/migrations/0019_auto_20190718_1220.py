# Generated by Django 2.1.2 on 2019-07-18 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Equipement', '0018_auto_20190718_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matr_panne_date',
            name='Date_Panne_FK',
        ),
        migrations.RemoveField(
            model_name='matr_panne_date',
            name='Materiel_FK',
        ),
        migrations.RemoveField(
            model_name='matr_panne_date',
            name='Panne_FK',
        ),
        migrations.RemoveField(
            model_name='panne',
            name='Type_Panne_FK',
        ),
        migrations.DeleteModel(
            name='Date_Panne',
        ),
        migrations.DeleteModel(
            name='Matr_Panne_Date',
        ),
        migrations.DeleteModel(
            name='Panne',
        ),
        migrations.DeleteModel(
            name='Type_Panne',
        ),
    ]
