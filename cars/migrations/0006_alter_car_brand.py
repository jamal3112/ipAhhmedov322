# Generated by Django 3.2 on 2021-04-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Марка машины'),
        ),
    ]
