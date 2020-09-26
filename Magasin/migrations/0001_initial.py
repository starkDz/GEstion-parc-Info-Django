# Generated by Django 2.2.3 on 2019-07-17 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Equipement', '0016_auto_20190717_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(default='/', max_length=250)),
                ('Quantite', models.PositiveIntegerField(default=1)),
                ('Marque_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipement.Marque')),
                ('Model_Article_FK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Equipement.Model_Materiel')),
                ('Service_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipement.Service')),
                ('Type_Article_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipement.Type_Materiel')),
            ],
            options={
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
