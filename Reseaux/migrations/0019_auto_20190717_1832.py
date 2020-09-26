# Generated by Django 2.2.3 on 2019-07-17 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reseaux', '0018_auto_20190717_1827'),
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
