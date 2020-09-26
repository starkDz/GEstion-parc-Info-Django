# Generated by Django 2.1.2 on 2018-12-28 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reseaux', '0007_auto_20181228_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armoire',
            name='type_armoire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reseaux.Type_arm'),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='armoire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reseaux.Armoire'),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='type_equipement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reseaux.Type_equipement'),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='usage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reseaux.Usage'),
        ),
    ]
