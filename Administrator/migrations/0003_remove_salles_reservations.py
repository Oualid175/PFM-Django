# Generated by Django 5.0 on 2023-12-31 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salles',
            name='reservations',
        ),
    ]
