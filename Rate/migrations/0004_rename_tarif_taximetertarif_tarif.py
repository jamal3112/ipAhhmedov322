# Generated by Django 3.2 on 2021-04-15 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rate', '0003_auto_20210415_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taximetertarif',
            old_name='Tarif',
            new_name='tarif',
        ),
    ]