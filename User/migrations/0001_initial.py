# Generated by Django 5.0 on 2023-12-31 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('nbr_invt', models.IntegerField()),
                ('equipment', models.ManyToManyField(related_name='reservations_set', to='Administrator.salles')),
                ('salle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salles', to='Administrator.salles')),
            ],
        ),
    ]