# Generated by Django 2.1.2 on 2018-12-28 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Equipement', '0011_auto_20181228_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc_Matr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_Doc', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Type_Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation_Type_Doc', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='materiel',
            name='Address_Ip',
            field=models.GenericIPAddressField(default='0.0.0.0'),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='Address_Mac',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='Masque',
            field=models.GenericIPAddressField(default='0.0.0.0'),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='Num_Serie',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='Passerelle',
            field=models.GenericIPAddressField(default='0.0.0.0'),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='Quantite',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='document',
            name='Type_Doc_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipement.Type_Document'),
        ),
        migrations.AddField(
            model_name='doc_matr',
            name='Document_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipement.Document'),
        ),
        migrations.AddField(
            model_name='doc_matr',
            name='Materiel_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipement.Materiel'),
        ),
    ]
