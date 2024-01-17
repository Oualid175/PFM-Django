# Generated by Django 5.0 on 2023-12-31 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salles',
            fields=[
                ('salle_id', models.AutoField(primary_key=True, serialize=False)),
                ('capacite', models.IntegerField()),
                ('equipment', models.ManyToManyField(related_name='salles_set', to='Administrator.equipment')),
            ],
        ),
    ]
